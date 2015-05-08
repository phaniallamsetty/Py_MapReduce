#!/bin/bash
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file sentLength_map.py sentLength_reduce.py -mapper sentLength_map.py -reducer sentLength_reduce.py
