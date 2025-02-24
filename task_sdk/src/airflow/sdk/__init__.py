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

from typing import TYPE_CHECKING

__all__ = [
    "__version__",
    "Asset",
    "AssetWatcher",
    "BaseOperator",
    "Connection",
    "DAG",
    "EdgeModifier",
    "Label",
    "MappedOperator",
    "TaskGroup",
    "XComArg",
    "dag",
    "get_current_context",
    "get_parsing_context",
]

__version__ = "1.0.0.alpha1"

if TYPE_CHECKING:
    from airflow.sdk.definitions.asset import Asset, AssetWatcher
    from airflow.sdk.definitions.baseoperator import BaseOperator
    from airflow.sdk.definitions.connection import Connection
    from airflow.sdk.definitions.context import get_current_context, get_parsing_context
    from airflow.sdk.definitions.dag import DAG, dag
    from airflow.sdk.definitions.edges import EdgeModifier, Label
    from airflow.sdk.definitions.mappedoperator import MappedOperator
    from airflow.sdk.definitions.taskgroup import TaskGroup
    from airflow.sdk.definitions.xcom_arg import XComArg

__lazy_imports: dict[str, str] = {
    "BaseOperator": ".definitions.baseoperator",
    "Connection": ".definitions.connection",
    "Param": ".definitions.param",
    "ParamsDict": ".definitions.param",
    "DAG": ".definitions.dag",
    "EdgeModifier": ".definitions.edges",
    "Label": ".definitions.edges",
    "MappedOperator": ".definitions.mappedoperator",
    "TaskGroup": ".definitions.taskgroup",
    "Variable": ".definitions.variable",
    "XComArg": ".definitions.xcom_arg",
    "dag": ".definitions.dag",
    "get_current_context": ".definitions.context",
    "get_parsing_context": ".definitions.context",
    "Asset": ".definitions.asset",
    "AssetWatcher": ".definitions.asset",
}


def __getattr__(name: str):
    if module_path := __lazy_imports.get(name):
        import importlib

        mod = importlib.import_module(module_path, __name__)
        val = getattr(mod, name)

        # Store for next time
        globals()[name] = val
        return val
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
