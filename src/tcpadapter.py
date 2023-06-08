from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
from spherov2.adapter.tcp_adapter import get_tcp_adapter

toy = scanner.find_toy(adapter=get_tcp_adapter('localhost'), toy_name="BB-EFF7")
with SpheroEduAPI(toy) as sphero:
    sphero.set_main_led(Color(77,160,244))