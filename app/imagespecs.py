# Copyright 2012 Mike Wakerly <opensource@hoho.com>
#
# This file is part of the Pykeg package of the Kegbot project.
# For more information on Pykeg or Kegbot, see http://kegbot.org/
#
# Pykeg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Pykeg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pykeg.  If not, see <http://www.gnu.org/licenses/>.

from imagekit.models import ImageSpecField
#kegbot uses ImageSpec, which is deprecated to the above.
from imagekit.processors import Adjust
from imagekit.processors import resize

resized = ImageSpecField(
    processors=[resize.ResizeToFit(1024, 1024)],
    source='image',
    format='JPEG',
    options={'quality': 90},
)

small_resized = ImageSpecField(
    processors=[resize.ResizeToFit(256, 256)],
    source='image',
    format='JPEG',
    options={'quality': 100},
)

thumbnail = ImageSpecField(
    processors=[Adjust(contrast=1.2, sharpness=1.1), resize.SmartResize(128, 128)],
    source='image',
    format='JPEG',
    options={'quality': 100},
)

small_thumbnail = ImageSpecField(
    processors=[Adjust(contrast=1.2, sharpness=1.1), resize.SmartResize(32, 32)],
    source='image',
    format='JPEG',
    options={'quality': 100},
)
