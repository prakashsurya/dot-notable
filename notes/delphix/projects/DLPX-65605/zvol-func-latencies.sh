#!/bin/bash

REGEXP="zvol_task_cb"
REGEXP+="|zvol_create_minors_impl"
REGEXP+="|zvol_remove_minors_impl"
REGEXP+="|zvol_rename_minors_impl"
REGEXP+="|zvol_set_snapdev_impl"
REGEXP+="|zvol_set_volmode_impl"

sudo /usr/share/bcc/tools/funclatency \
	--timestamp \
	--function \
	--milliseconds \
	--interval 10 \
	--duration 60 \
	--regexp "$REGEXP"
