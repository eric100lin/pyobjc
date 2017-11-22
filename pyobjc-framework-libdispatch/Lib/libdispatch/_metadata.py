# This file is generated by objective.metadata
#
# Last update: Wed Nov 22 12:49:26 2017

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
misc.update({'timespec': objc.createStructType('timespec', b'{timespec=ll}', ['tv_sec', 'tv_nsec'])})
constants = '''$$'''
enums = '''$DISPATCH_BLOCK_ASSIGN_CURRENT@4$DISPATCH_BLOCK_BARRIER@1$DISPATCH_BLOCK_DETACHED@2$DISPATCH_BLOCK_ENFORCE_QOS_CLASS@32$DISPATCH_BLOCK_INHERIT_QOS_CLASS@16$DISPATCH_BLOCK_NO_QOS_CLASS@8$DISPATCH_IO_RANDOM@1$DISPATCH_IO_STREAM@0$DISPATCH_TIME_FOREVER@18446744073709551615$DISPATCH_TIME_NOW@0$NSEC_PER_MSEC@1000000$NSEC_PER_SEC@1000000000$NSEC_PER_USEC@1000$USEC_PER_SEC@1000000$'''
misc.update({})
functions={'dispatch_group_enter': (b'v@',), 'dispatch_activate': (b'v@',), 'dispatch_block_cancel': (b'v@?', '', {'arguments': {0: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_group_async_f': (b'v@@^v^?', '', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_walltime': (b'Qn^{timespec=ll}q',), 'dispatch_testcancel': (b'l@',), 'dispatch_group_leave': (b'v@',), 'dispatch_resume': (b'v@',), 'dispatch_set_context': (b'v@^v',), 'dispatch_notify': (b'v@?@@?', '', {'arguments': {0: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}, 2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_suspend': (b'v@',), 'dispatch_write': (b'vi@@@?', '', {'arguments': {1: {'comment': 'dispatch_data_t'}, 3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}, 1: {'comment': 'dispatch_data_t', 'type': '@'}, 2: {'type': 'i'}}}}}}), 'dispatch_set_finalizer_f': (b'v@^?', '', {'arguments': {1: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}, 'callable_retained': True}}}), 'dispatch_group_notify_f': (b'v@@^v^?', '', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_block_create': (b'@?L@?', '', {'retval': {'callable': {'retval': {'type': 'v'}, 'arguments': {0: {'type': '^v'}}}, 'already_retained': True}, 'arguments': {1: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_wait': (b'l@Q',), 'dispatch_group_notify': (b'v@@@?', '', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_block_perform': (b'vL@?', '', {'arguments': {1: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_block_notify': (b'v@?@@?', '', {'arguments': {0: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}, 2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_group_async': (b'v@@@?', '', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_block_create_with_qos_class': (b'@?LIi@?', '', {'retval': {'callable': {'retval': {'type': 'v'}, 'arguments': {0: {'type': '^v'}}}, 'already_retained': True}, 'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_cancel': (b'v@',), 'dispatch_group_wait': (b'l@Q',), 'dispatch_block_testcancel': (b'l@?', '', {'arguments': {0: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_block_wait': (b'l@?Q', '', {'arguments': {0: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_read': (b'viL@@?', '', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}, 1: {'comment': 'dispatch_data_t', 'type': '@'}, 2: {'type': 'i'}}}}}}), 'dispatch_group_create': (b'v',), 'dispatch_once': (b'vN^l@?', '', {'arguments': {0: {'c_array_of_fixed_length': 1}, 1: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}}}}), 'dispatch_once_f': (b'vN^l^v^?', '', {'arguments': {0: {'c_array_of_fixed_length': 1}, 2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}}}, 'callable_retained': False}}}), 'dispatch_get_context': (b'^v@',), 'dispatch_time': (b'QQq',)}
expressions = {}

# END OF FILE
