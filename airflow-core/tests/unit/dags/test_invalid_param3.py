# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

from datetime import datetime

from airflow.models import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk.definitions.param import Param

with DAG(
    "test_invalid_param3",
    start_date=datetime(2021, 1, 1),
    schedule="0 0 * * *",
    params={
        # a mandatory number param but pass a string as default value
        "int_param": Param(default="banana", type="integer"),
    },
) as the_dag:

    def print_these(*params):
        for param in params:
            print(param)

    PythonOperator(
        task_id="ref_params",
        python_callable=print_these,
        op_args=[
            "{{ params.int_param }}",
        ],
    )
