import logging
import time
from airflow.operators.sensors import BaseSensorOperator
from airflow.utils.decorators import apply_defaults


class SampleSensor(BaseSensorOperator):
	template_fields = ['run_id']

	@apply_defaults
	def __init__(self, run_id, *args, **kwargs):
		self.run_id = run_id
		self.counter = 0
		super(SampleSensor, self).__init__(*args, **kwargs)

	def poke(self, context):
		self.counter += 1
		logging.info("Poking: Sample Sensor <<{}>> - counter {}".format(self.run_id, self.counter))

		return self.counter == 10



