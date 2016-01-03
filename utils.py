# -*- coding: utf-8 -*-

import string
import random

def random_string_gen(size=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(size))
