# -*- coding: utf-8 -*-
#
# This file is part of CERN Document Server.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""CDS To MARC21 model."""

from __future__ import absolute_import, unicode_literals

from dojson.contrib.to_marc21 import to_marc21
from dojson.contrib.to_marc21.model import OverUndo

from ...marc21.models.default import CDSMarc21


class CDSToMarc21(CDSMarc21, OverUndo):

    """Translation Index for CDS specific MARC21."""

    __query__ = 'subject_indicator:CERN'


model = CDSToMarc21(bases=(to_marc21, ),
                    entry_point_group='cds_dojson.to_marc21.default')