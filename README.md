# ExperimentalRobotsAss1

There is a launch file to run all necessary nodes.

I divided everything into three pkg:

-command_transmiter: it is a talker that sends if to enter the play state and sends for now two numbers which is the position of the person.
-fsm: which presents the fsm which has a listener to receive commands and a talker to send the position to reach which also in this case are two values ​​x and y.
-position_receiver: which presents a listener that takes the position to reach from the fsm.
