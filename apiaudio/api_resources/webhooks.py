import hmac
import time
from hashlib import sha256


class Webhooks(object):
    DEFAULT_TOLERANCE = 300

    @staticmethod
    def verify(payload, sig_header, secret, tolerance=DEFAULT_TOLERANCE):
        if hasattr(payload, "decode"):
            payload = payload.decode("utf-8")

        WebhookSignature.verify_header(payload, sig_header, secret, tolerance)

        return True


class WebhookSignature(object):
    EXPECTED_SCHEME = "v1"

    @staticmethod
    def _compute_signature(payload, secret):
        mac = hmac.new(
            secret.encode("utf-8"),
            msg=payload.encode("utf-8"),
            digestmod=sha256,
        )
        return mac.hexdigest()

    @staticmethod
    def _get_timestamp_and_signatures(header, scheme):
        list_items = [i.split("=", 2) for i in header.split(",")]
        timestamp = int([i[1] for i in list_items if i[0] == "t"][0])
        signatures = [i[1] for i in list_items if i[0] == scheme]
        return timestamp, signatures

    @classmethod
    def verify_header(cls, payload, header, secret, tolerance=None):
        try:
            timestamp, signatures = cls._get_timestamp_and_signatures(
                header, cls.EXPECTED_SCHEME
            )
        except Exception:
            raise Exception(
                "Unable to extract timestamp and signatures from header",
                header,
                payload,
            )

        if not signatures:
            raise Exception(
                "No signatures found with expected scheme " "%s" % cls.EXPECTED_SCHEME,
                header,
                payload,
            )

        signed_payload = "%d.%s" % (timestamp, payload)
        expected_sig = cls._compute_signature(signed_payload, secret)

        if not any(expected_sig == s for s in signatures):
            raise Exception(
                "No signatures found matching the expected signature for " "payload",
                header,
                payload,
            )

        if tolerance and timestamp < time.time() - tolerance:
            raise Exception(
                "Timestamp outside the tolerance zone (%d)" % timestamp,
                header,
                payload,
            )

        return True
