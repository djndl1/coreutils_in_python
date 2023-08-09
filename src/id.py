#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, pwd, grp

from typing import Tuple, Iterable, List

def retrieve_users(user_name: str = None) -> Tuple[Tuple[int, str], Tuple[int, str]]:
    real_id = None
    effective_id = None
    if user_name:
        real_id = pwd.getpwnam(user_name).pw_uid
        effective_id = real_id
    else:
        real_id, effective_id, _ = os.getresuid()

    return tuple((i, pwd.getpwuid(i).pw_name) for i in (real_id, effective_id))

def retrieve_groups(user_name: str = None) -> Tuple[Tuple[int, str], Tuple[int, str], List[Tuple[int, str]]]:
    gids = (0, 0)
    supplemental_group_ids = []
    if user_name:
        real_gid = pwd.getpwnam(user_name).pw_gid
        gids = (real_gid, real_gid)
        supplemental_group_ids = os.getgrouplist(user_name, real_gid)
        supplemental_group_ids.remove(real_gid)
    else:
        real_gid, effective_gid, _ = os.getresgid()
        gids = (real_gid, effective_gid)
        supplemental_group_ids = os.getgroups()

    dgrps = [(g.gr_gid, g.gr_name) for g in [grp.getgrgid(i) for i in gids]]
    sgrps = [(g.gr_gid, g.gr_name) for g in [grp.getgrgid(i) for i in supplemental_group_ids]]

    return (dgrps[0], dgrps[1], sgrps)
