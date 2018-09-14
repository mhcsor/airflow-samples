from airflow.plugins_manager import AirflowPlugin
from sample_plugin.operators.sample_operator import SampleOperator
from sample_plugin.sensors.sample_sensor import SampleSensor


class SamplePlugin(AirflowPlugin):
	name = "sample_plugin"
	hooks = []
	operators = [SampleOperator, SampleSensor]
	executors = []
	macros = []
	admin_views = []
	flask_blueprints = []
	menu_links = []