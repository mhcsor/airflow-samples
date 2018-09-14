import logging
import time
from airflow.models import BaseOperator, SkipMixin
from airflow.utils.decorators import apply_defaults


class SampleOperator(BaseOperator):
	template_fields = []
	template_ext = ()
	ui_color = '#f9c915'

	def __init__(self, *args, **kwargs):
		super(SampleOperator, self).__init__(*args, **kwargs)

	def execute(self, context):
		logging.info("Executing Sample Operator")
		return "Sample XCOM"