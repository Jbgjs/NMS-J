from sqlalchemy import ForeignKey, Integer

from elimNMS.database import db
from elimNMS.forms import DeviceForm
from elimNMS.fields import HiddenField, StringField
from elimNMS.models.inventory import Device


class Router(Device):
    __tablename__ = "router"
    __mapper_args__ = {"polymorphic_identity": "router"}
    pretty_name = "Router"
    id = db.Column(Integer, ForeignKey("device.id"), primary_key=True)
    serial_number = db.Column(db.SmallString)


class RouterForm(DeviceForm):
    form_type = HiddenField(default="router")
    serial_number = StringField("Serial Number")
    properties = ["serial_number"]
