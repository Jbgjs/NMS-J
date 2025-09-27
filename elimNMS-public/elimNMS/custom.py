from re import sub
from uuid import uuid4
from warnings import warn

try:
    from ldap3 import Connection
except ImportError as exc:
    warn(f"ldap3 모듈을 가져올 수 없습니다.({exc})")

from elimNMS.environment import env
from elimNMS.variables import vs

class CustomApp:
    def ldap_authentication(self, user, name, password):
        if not hasattr(env, "ldap_server"):
            env.log("error", "LDAP 인증 실패: 서버가 구성되지 않았습니다")
            return False
        user = f"uid={name},dc=example,dc=com"
        success = Connection(env.ldap_server, user=user, password=password).bind()
        return {"name": name, "is_admin": True} if success else False

    def tacacs_authentication(self, user, name, password):
        if not hasattr(env, "tacacs_client"):
            env.log("error", "TACACS+ 인증 실패: 클라이언트가 구성되지 않았습니다")
            return False
        success = env.tacacs_client.authenticate(name, password).valid
        return {"name": name, "is_admin": True} if success else False

    def parse_configuration_property(self, device, property, value=None):
        if not value:
            value = getattr(device, property)
        if device.operating_system == "EOS" and property == "configuration":
            value = sub(r"(username.*secret) (.*)", r"\g<1> ********", value)
        return value

    def generate_uuid(self):
        return str(uuid4())

    def run_post_processing(self, run, run_result):
        if run.is_main_run:
            env.log(
                "info",
                (
                    f"RUNTIME {run_result['runtime']} - USER {run.creator} -"
                    f"SERVICE '{run_result['properties']['scoped_name']}' - "
                    f"Completed in {run_result['duration']}"
                ),
            )


vs.custom = CustomApp()
