from typing import Literal, Optional, List, Union

from apiaudio.api_request import APIRequest

from apiaudio.logging import SDKLogger

_logger = SDKLogger(level="INFO")


class UsersManager(APIRequest):
    """
    CRUD interface for Users resource.

    ...

    Notes:
    - A user should represent a single person/voice
    - Verticals are assigned to a user
    - Uploaded files belong to a user
    - Trained models belong to a user

    """

    OBJECT_NAME = "VC_Users"
    resource_path = "/ulvc2/users"

    class User(object):
        """
        Representation of a voice cloner user.
        """

        def __init__(
            self,
            id: str,
            name: Optional[str],
            gender: Optional[Literal["male", "female", "non-binary", ""]],
            availableVerticals: Optional[list],
            selectedVerticals: Optional[list],
            metadata: Optional[dict],
            voiceCloningEnabled: Optional[bool],
            createdAt: str,
            **kwargs,
        ):
            self.id = id
            self.name = name
            self.gender = gender
            self.available_verticals = availableVerticals
            self.selected_verticals = selectedVerticals
            self.metadata = metadata
            self.voice_cloning_enabled = voiceCloningEnabled
            self.created_at = createdAt

        def get_recording_session(self) -> object:  # session object
            pass

        def add_recording(self, audio: bytes, utterance: object) -> None:
            pass

        def trigger_model_training(
            self, name: str = "", verticals_to_use: list = []
        ) -> None:
            pass

    @classmethod
    def create(
        cls,
        id: str = "",
        name: str = "",
        gender: Literal["male", "female", "non-binary", ""] = "",
        available_verticals: list = [],
        selected_verticals: list = [],
        metadata: dict = {},
        voice_cloning_enabled: bool = False,
    ) -> User:
        """
        Create a new user.

        :param id: The user's id. If not provided, it will be generated through uuid4 method.
        :param name: the name of the user
        :param gender: the gender of the user - male/female/non-binary
        :param available_verticals: verticals which can be selected by the user.
        :param selected_verticals: verticals that are served to the user in recording session
        :param metadata: additional information about the user
        :param voice_cloning_enabled: whether the user is allowed to use voice cloning feature
        """
        data = cls._post_request(
            json={
                "id": id,
                "name": name,
                "gender": gender,
                "availableVerticals": available_verticals,
                "selectedVerticals": selected_verticals,
                "metadata": metadata,
                "voiceCloningEnabled": voice_cloning_enabled,
            }
        ).get("data", {})

        return cls.User(**data)

    @classmethod
    def list(cls) -> List[User]:
        """
        List all existing users.
        """
        data = cls._get_request().get("data", {})

        return [cls.User(**user) for user in data]

    @classmethod
    def retrieve(cls, id: str) -> User:
        """
        Retrieve a user by id.
        """
        data = cls._get_request(path_param=f"{cls.resource_path}/{id}").get("data", {})

        return cls.User(**data)

    @classmethod
    def update(cls, user: User) -> None:
        """
        Update the user. The passed user object gets updated.
        """
        data = cls._patch_request(json=vars(user), path_param=user.id).get("data", {})

        user.__init__(**data)

    @classmethod
    def delete(cls, user: Union[User, str]) -> None:
        """
        Delete the user.
        When passing the user object, all its attributes are set to None.
        """
        if isinstance(user, str):
            user_id = user
        elif isinstance(user, cls.User):
            user_id = user.id

        cls._delete_request(path_param=f"{cls.resource_path}/{user_id}").get("data", {})
        for key in vars(user).keys():
            setattr(user, key, None)
