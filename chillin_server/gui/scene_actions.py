# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class BaseAction(object):

	@staticmethod
	def name():
		return 'BaseAction'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None):
		self.initialize(cycle, ref, child_ref, duration_cycles)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None):
		self.cycle = cycle
		self.ref = ref
		self.child_ref = child_ref
		self.duration_cycles = duration_cycles
	

	def serialize(self):
		s = b''
		
		# serialize self.cycle
		s += b'\x00' if self.cycle is None else b'\x01'
		if self.cycle is not None:
			s += struct.pack('f', self.cycle)
		
		# serialize self.ref
		s += b'\x00' if self.ref is None else b'\x01'
		if self.ref is not None:
			s += struct.pack('i', self.ref)
		
		# serialize self.child_ref
		s += b'\x00' if self.child_ref is None else b'\x01'
		if self.child_ref is not None:
			tmp0 = b''
			tmp0 += struct.pack('I', len(self.child_ref))
			while len(tmp0) and tmp0[-1] == b'\x00'[0]:
				tmp0 = tmp0[:-1]
			s += struct.pack('B', len(tmp0))
			s += tmp0
			
			s += self.child_ref.encode('ISO-8859-1') if PY3 else self.child_ref
		
		# serialize self.duration_cycles
		s += b'\x00' if self.duration_cycles is None else b'\x01'
		if self.duration_cycles is not None:
			s += struct.pack('f', self.duration_cycles)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.cycle
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			self.cycle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.cycle = None
		
		# deserialize self.ref
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			self.ref = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.ref = None
		
		# deserialize self.child_ref
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp5 = s[offset:offset + tmp4]
			offset += tmp4
			tmp5 += b'\x00' * (4 - tmp4)
			tmp6 = struct.unpack('I', tmp5)[0]
			
			self.child_ref = s[offset:offset + tmp6].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp6]
			offset += tmp6
		else:
			self.child_ref = None
		
		# deserialize self.duration_cycles
		tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp7:
			self.duration_cycles = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.duration_cycles = None
		
		return offset


class Vector2(object):

	@staticmethod
	def name():
		return 'Vector2'


	def __init__(self, x=None, y=None):
		self.initialize(x, y)
	

	def initialize(self, x=None, y=None):
		self.x = x
		self.y = y
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('f', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('f', self.y)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp8:
			self.x = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp9 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp9:
			self.y = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		return offset


class Vector3(object):

	@staticmethod
	def name():
		return 'Vector3'


	def __init__(self, x=None, y=None, z=None):
		self.initialize(x, y, z)
	

	def initialize(self, x=None, y=None, z=None):
		self.x = x
		self.y = y
		self.z = z
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('f', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('f', self.y)
		
		# serialize self.z
		s += b'\x00' if self.z is None else b'\x01'
		if self.z is not None:
			s += struct.pack('f', self.z)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp10 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp10:
			self.x = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp11 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp11:
			self.y = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		# deserialize self.z
		tmp12 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp12:
			self.z = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.z = None
		
		return offset


class Vector4(object):

	@staticmethod
	def name():
		return 'Vector4'


	def __init__(self, x=None, y=None, z=None, w=None):
		self.initialize(x, y, z, w)
	

	def initialize(self, x=None, y=None, z=None, w=None):
		self.x = x
		self.y = y
		self.z = z
		self.w = w
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('f', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('f', self.y)
		
		# serialize self.z
		s += b'\x00' if self.z is None else b'\x01'
		if self.z is not None:
			s += struct.pack('f', self.z)
		
		# serialize self.w
		s += b'\x00' if self.w is None else b'\x01'
		if self.w is not None:
			s += struct.pack('f', self.w)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp13 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp13:
			self.x = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp14 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp14:
			self.y = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		# deserialize self.z
		tmp15 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp15:
			self.z = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.z = None
		
		# deserialize self.w
		tmp16 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp16:
			self.w = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.w = None
		
		return offset


class Asset(object):

	@staticmethod
	def name():
		return 'Asset'


	def __init__(self, bundle_name=None, asset_name=None):
		self.initialize(bundle_name, asset_name)
	

	def initialize(self, bundle_name=None, asset_name=None):
		self.bundle_name = bundle_name
		self.asset_name = asset_name
	

	def serialize(self):
		s = b''
		
		# serialize self.bundle_name
		s += b'\x00' if self.bundle_name is None else b'\x01'
		if self.bundle_name is not None:
			tmp17 = b''
			tmp17 += struct.pack('I', len(self.bundle_name))
			while len(tmp17) and tmp17[-1] == b'\x00'[0]:
				tmp17 = tmp17[:-1]
			s += struct.pack('B', len(tmp17))
			s += tmp17
			
			s += self.bundle_name.encode('ISO-8859-1') if PY3 else self.bundle_name
		
		# serialize self.asset_name
		s += b'\x00' if self.asset_name is None else b'\x01'
		if self.asset_name is not None:
			tmp18 = b''
			tmp18 += struct.pack('I', len(self.asset_name))
			while len(tmp18) and tmp18[-1] == b'\x00'[0]:
				tmp18 = tmp18[:-1]
			s += struct.pack('B', len(tmp18))
			s += tmp18
			
			s += self.asset_name.encode('ISO-8859-1') if PY3 else self.asset_name
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.bundle_name
		tmp19 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp19:
			tmp20 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp21 = s[offset:offset + tmp20]
			offset += tmp20
			tmp21 += b'\x00' * (4 - tmp20)
			tmp22 = struct.unpack('I', tmp21)[0]
			
			self.bundle_name = s[offset:offset + tmp22].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp22]
			offset += tmp22
		else:
			self.bundle_name = None
		
		# deserialize self.asset_name
		tmp23 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp23:
			tmp24 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp25 = s[offset:offset + tmp24]
			offset += tmp24
			tmp25 += b'\x00' * (4 - tmp24)
			tmp26 = struct.unpack('I', tmp25)[0]
			
			self.asset_name = s[offset:offset + tmp26].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp26]
			offset += tmp26
		else:
			self.asset_name = None
		
		return offset


class BaseCreation(BaseAction):

	@staticmethod
	def name():
		return 'BaseCreation'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.parent_ref = parent_ref
		self.parent_child_ref = parent_child_ref
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.parent_ref
		s += b'\x00' if self.parent_ref is None else b'\x01'
		if self.parent_ref is not None:
			s += struct.pack('i', self.parent_ref)
		
		# serialize self.parent_child_ref
		s += b'\x00' if self.parent_child_ref is None else b'\x01'
		if self.parent_child_ref is not None:
			tmp27 = b''
			tmp27 += struct.pack('I', len(self.parent_child_ref))
			while len(tmp27) and tmp27[-1] == b'\x00'[0]:
				tmp27 = tmp27[:-1]
			s += struct.pack('B', len(tmp27))
			s += tmp27
			
			s += self.parent_child_ref.encode('ISO-8859-1') if PY3 else self.parent_child_ref
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.parent_ref
		tmp28 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp28:
			self.parent_ref = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.parent_ref = None
		
		# deserialize self.parent_child_ref
		tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp29:
			tmp30 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp31 = s[offset:offset + tmp30]
			offset += tmp30
			tmp31 += b'\x00' * (4 - tmp30)
			tmp32 = struct.unpack('I', tmp31)[0]
			
			self.parent_child_ref = s[offset:offset + tmp32].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp32]
			offset += tmp32
		else:
			self.parent_child_ref = None
		
		return offset


class CreateEmptyGameObject(BaseCreation):

	@staticmethod
	def name():
		return 'CreateEmptyGameObject'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None):
		BaseCreation.initialize(self, cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref)
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseCreation.serialize(self)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseCreation.deserialize(self, s, offset)
		
		return offset


class InstantiateBundleAsset(BaseCreation):

	@staticmethod
	def name():
		return 'InstantiateBundleAsset'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None, asset=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref, asset)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None, asset=None):
		BaseCreation.initialize(self, cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref)
		
		self.asset = asset
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseCreation.serialize(self)
		
		# serialize self.asset
		s += b'\x00' if self.asset is None else b'\x01'
		if self.asset is not None:
			s += self.asset.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseCreation.deserialize(self, s, offset)
		
		# deserialize self.asset
		tmp33 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp33:
			self.asset = Asset()
			offset = self.asset.deserialize(s, offset)
		else:
			self.asset = None
		
		return offset


class EBasicObjectType(Enum):
	Sprite = 0
	AudioSource = 1
	Ellipse2D = 2
	Polygon2D = 3
	Line = 4
	Light = 5


class CreateBasicObject(BaseCreation):

	@staticmethod
	def name():
		return 'CreateBasicObject'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None, type=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref, type)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None, type=None):
		BaseCreation.initialize(self, cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref)
		
		self.type = type
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseCreation.serialize(self)
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			s += struct.pack('b', self.type.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseCreation.deserialize(self, s, offset)
		
		# deserialize self.type
		tmp34 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp34:
			tmp35 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = EBasicObjectType(tmp35)
		else:
			self.type = None
		
		return offset


class EUIElementType(Enum):
	Canvas = 0
	Text = 1
	Slider = 2
	RawImage = 3
	Panel = 4


class CreateUIElement(BaseCreation):

	@staticmethod
	def name():
		return 'CreateUIElement'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None, type=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref, type)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, parent_ref=None, parent_child_ref=None, type=None):
		BaseCreation.initialize(self, cycle, ref, child_ref, duration_cycles, parent_ref, parent_child_ref)
		
		self.type = type
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseCreation.serialize(self)
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			s += struct.pack('b', self.type.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseCreation.deserialize(self, s, offset)
		
		# deserialize self.type
		tmp36 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp36:
			tmp37 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = EUIElementType(tmp37)
		else:
			self.type = None
		
		return offset


class Destroy(BaseAction):

	@staticmethod
	def name():
		return 'Destroy'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None):
		self.initialize(cycle, ref, child_ref, duration_cycles)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		return offset


class ChangeVisibility(BaseAction):

	@staticmethod
	def name():
		return 'ChangeVisibility'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, is_visible=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, is_visible)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, is_visible=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.is_visible = is_visible
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.is_visible
		s += b'\x00' if self.is_visible is None else b'\x01'
		if self.is_visible is not None:
			s += struct.pack('?', self.is_visible)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.is_visible
		tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp38:
			self.is_visible = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_visible = None
		
		return offset


class ChangeTransform(BaseAction):

	@staticmethod
	def name():
		return 'ChangeTransform'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, position=None, rotation=None, scale=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, position, rotation, scale)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, position=None, rotation=None, scale=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.position = position
		self.rotation = rotation
		self.scale = scale
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += self.position.serialize()
		
		# serialize self.rotation
		s += b'\x00' if self.rotation is None else b'\x01'
		if self.rotation is not None:
			s += self.rotation.serialize()
		
		# serialize self.scale
		s += b'\x00' if self.scale is None else b'\x01'
		if self.scale is not None:
			s += self.scale.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.position
		tmp39 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp39:
			self.position = Vector3()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.rotation
		tmp40 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp40:
			self.rotation = Vector3()
			offset = self.rotation.deserialize(s, offset)
		else:
			self.rotation = None
		
		# deserialize self.scale
		tmp41 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp41:
			self.scale = Vector3()
			offset = self.scale.deserialize(s, offset)
		else:
			self.scale = None
		
		return offset


class EAnimatorVariableType(Enum):
	Int = 0
	Float = 1
	Bool = 2
	Trigger = 3


class ChangeAnimatorVariable(BaseAction):

	@staticmethod
	def name():
		return 'ChangeAnimatorVariable'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, var_name=None, var_type=None, int_value=None, float_value=None, bool_value=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, var_name, var_type, int_value, float_value, bool_value)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, var_name=None, var_type=None, int_value=None, float_value=None, bool_value=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.var_name = var_name
		self.var_type = var_type
		self.int_value = int_value
		self.float_value = float_value
		self.bool_value = bool_value
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.var_name
		s += b'\x00' if self.var_name is None else b'\x01'
		if self.var_name is not None:
			tmp42 = b''
			tmp42 += struct.pack('I', len(self.var_name))
			while len(tmp42) and tmp42[-1] == b'\x00'[0]:
				tmp42 = tmp42[:-1]
			s += struct.pack('B', len(tmp42))
			s += tmp42
			
			s += self.var_name.encode('ISO-8859-1') if PY3 else self.var_name
		
		# serialize self.var_type
		s += b'\x00' if self.var_type is None else b'\x01'
		if self.var_type is not None:
			s += struct.pack('b', self.var_type.value)
		
		# serialize self.int_value
		s += b'\x00' if self.int_value is None else b'\x01'
		if self.int_value is not None:
			s += struct.pack('i', self.int_value)
		
		# serialize self.float_value
		s += b'\x00' if self.float_value is None else b'\x01'
		if self.float_value is not None:
			s += struct.pack('f', self.float_value)
		
		# serialize self.bool_value
		s += b'\x00' if self.bool_value is None else b'\x01'
		if self.bool_value is not None:
			s += struct.pack('?', self.bool_value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.var_name
		tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp43:
			tmp44 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp45 = s[offset:offset + tmp44]
			offset += tmp44
			tmp45 += b'\x00' * (4 - tmp44)
			tmp46 = struct.unpack('I', tmp45)[0]
			
			self.var_name = s[offset:offset + tmp46].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp46]
			offset += tmp46
		else:
			self.var_name = None
		
		# deserialize self.var_type
		tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp47:
			tmp48 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.var_type = EAnimatorVariableType(tmp48)
		else:
			self.var_type = None
		
		# deserialize self.int_value
		tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp49:
			self.int_value = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.int_value = None
		
		# deserialize self.float_value
		tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp50:
			self.float_value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.float_value = None
		
		# deserialize self.bool_value
		tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp51:
			self.bool_value = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.bool_value = None
		
		return offset


class ChangeAnimatorState(BaseAction):

	@staticmethod
	def name():
		return 'ChangeAnimatorState'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, state_name=None, layer=None, normalized_time=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, state_name, layer, normalized_time)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, state_name=None, layer=None, normalized_time=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.state_name = state_name
		self.layer = layer
		self.normalized_time = normalized_time
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.state_name
		s += b'\x00' if self.state_name is None else b'\x01'
		if self.state_name is not None:
			tmp52 = b''
			tmp52 += struct.pack('I', len(self.state_name))
			while len(tmp52) and tmp52[-1] == b'\x00'[0]:
				tmp52 = tmp52[:-1]
			s += struct.pack('B', len(tmp52))
			s += tmp52
			
			s += self.state_name.encode('ISO-8859-1') if PY3 else self.state_name
		
		# serialize self.layer
		s += b'\x00' if self.layer is None else b'\x01'
		if self.layer is not None:
			s += struct.pack('i', self.layer)
		
		# serialize self.normalized_time
		s += b'\x00' if self.normalized_time is None else b'\x01'
		if self.normalized_time is not None:
			s += struct.pack('f', self.normalized_time)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.state_name
		tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp53:
			tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp55 = s[offset:offset + tmp54]
			offset += tmp54
			tmp55 += b'\x00' * (4 - tmp54)
			tmp56 = struct.unpack('I', tmp55)[0]
			
			self.state_name = s[offset:offset + tmp56].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp56]
			offset += tmp56
		else:
			self.state_name = None
		
		# deserialize self.layer
		tmp57 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp57:
			self.layer = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.layer = None
		
		# deserialize self.normalized_time
		tmp58 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp58:
			self.normalized_time = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.normalized_time = None
		
		return offset


class ChangeAudioSource(BaseAction):

	@staticmethod
	def name():
		return 'ChangeAudioSource'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, audio_clip_asset=None, time=None, mute=None, loop=None, priority=None, volume=None, spatial_blend=None, play=None, stop=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, audio_clip_asset, time, mute, loop, priority, volume, spatial_blend, play, stop)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, audio_clip_asset=None, time=None, mute=None, loop=None, priority=None, volume=None, spatial_blend=None, play=None, stop=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.audio_clip_asset = audio_clip_asset
		self.time = time
		self.mute = mute
		self.loop = loop
		self.priority = priority
		self.volume = volume
		self.spatial_blend = spatial_blend
		self.play = play
		self.stop = stop
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.audio_clip_asset
		s += b'\x00' if self.audio_clip_asset is None else b'\x01'
		if self.audio_clip_asset is not None:
			s += self.audio_clip_asset.serialize()
		
		# serialize self.time
		s += b'\x00' if self.time is None else b'\x01'
		if self.time is not None:
			s += struct.pack('f', self.time)
		
		# serialize self.mute
		s += b'\x00' if self.mute is None else b'\x01'
		if self.mute is not None:
			s += struct.pack('?', self.mute)
		
		# serialize self.loop
		s += b'\x00' if self.loop is None else b'\x01'
		if self.loop is not None:
			s += struct.pack('?', self.loop)
		
		# serialize self.priority
		s += b'\x00' if self.priority is None else b'\x01'
		if self.priority is not None:
			s += struct.pack('i', self.priority)
		
		# serialize self.volume
		s += b'\x00' if self.volume is None else b'\x01'
		if self.volume is not None:
			s += struct.pack('f', self.volume)
		
		# serialize self.spatial_blend
		s += b'\x00' if self.spatial_blend is None else b'\x01'
		if self.spatial_blend is not None:
			s += struct.pack('f', self.spatial_blend)
		
		# serialize self.play
		s += b'\x00' if self.play is None else b'\x01'
		if self.play is not None:
			s += struct.pack('?', self.play)
		
		# serialize self.stop
		s += b'\x00' if self.stop is None else b'\x01'
		if self.stop is not None:
			s += struct.pack('?', self.stop)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.audio_clip_asset
		tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp59:
			self.audio_clip_asset = Asset()
			offset = self.audio_clip_asset.deserialize(s, offset)
		else:
			self.audio_clip_asset = None
		
		# deserialize self.time
		tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp60:
			self.time = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.time = None
		
		# deserialize self.mute
		tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp61:
			self.mute = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.mute = None
		
		# deserialize self.loop
		tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp62:
			self.loop = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.loop = None
		
		# deserialize self.priority
		tmp63 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp63:
			self.priority = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.priority = None
		
		# deserialize self.volume
		tmp64 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp64:
			self.volume = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.volume = None
		
		# deserialize self.spatial_blend
		tmp65 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp65:
			self.spatial_blend = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.spatial_blend = None
		
		# deserialize self.play
		tmp66 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp66:
			self.play = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.play = None
		
		# deserialize self.stop
		tmp67 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp67:
			self.stop = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.stop = None
		
		return offset


class ChangeRectTransform(BaseAction):

	@staticmethod
	def name():
		return 'ChangeRectTransform'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, position=None, rotation=None, scale=None, pivot=None, anchor_min=None, anchor_max=None, size=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, position, rotation, scale, pivot, anchor_min, anchor_max, size)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, position=None, rotation=None, scale=None, pivot=None, anchor_min=None, anchor_max=None, size=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.position = position
		self.rotation = rotation
		self.scale = scale
		self.pivot = pivot
		self.anchor_min = anchor_min
		self.anchor_max = anchor_max
		self.size = size
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += self.position.serialize()
		
		# serialize self.rotation
		s += b'\x00' if self.rotation is None else b'\x01'
		if self.rotation is not None:
			s += self.rotation.serialize()
		
		# serialize self.scale
		s += b'\x00' if self.scale is None else b'\x01'
		if self.scale is not None:
			s += self.scale.serialize()
		
		# serialize self.pivot
		s += b'\x00' if self.pivot is None else b'\x01'
		if self.pivot is not None:
			s += self.pivot.serialize()
		
		# serialize self.anchor_min
		s += b'\x00' if self.anchor_min is None else b'\x01'
		if self.anchor_min is not None:
			s += self.anchor_min.serialize()
		
		# serialize self.anchor_max
		s += b'\x00' if self.anchor_max is None else b'\x01'
		if self.anchor_max is not None:
			s += self.anchor_max.serialize()
		
		# serialize self.size
		s += b'\x00' if self.size is None else b'\x01'
		if self.size is not None:
			s += self.size.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.position
		tmp68 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp68:
			self.position = Vector3()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.rotation
		tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp69:
			self.rotation = Vector3()
			offset = self.rotation.deserialize(s, offset)
		else:
			self.rotation = None
		
		# deserialize self.scale
		tmp70 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp70:
			self.scale = Vector3()
			offset = self.scale.deserialize(s, offset)
		else:
			self.scale = None
		
		# deserialize self.pivot
		tmp71 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp71:
			self.pivot = Vector2()
			offset = self.pivot.deserialize(s, offset)
		else:
			self.pivot = None
		
		# deserialize self.anchor_min
		tmp72 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp72:
			self.anchor_min = Vector2()
			offset = self.anchor_min.deserialize(s, offset)
		else:
			self.anchor_min = None
		
		# deserialize self.anchor_max
		tmp73 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp73:
			self.anchor_max = Vector2()
			offset = self.anchor_max.deserialize(s, offset)
		else:
			self.anchor_max = None
		
		# deserialize self.size
		tmp74 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp74:
			self.size = Vector2()
			offset = self.size.deserialize(s, offset)
		else:
			self.size = None
		
		return offset


class ETextAlignmentOption(Enum):
	TopLeft = 257
	Top = 258
	TopRight = 260
	TopJustified = 264
	TopFlush = 272
	TopGeoAligned = 288
	Left = 513
	Center = 514
	Right = 516
	Justified = 520
	Flush = 528
	CenterGeoAligned = 544
	BottomLeft = 1025
	Bottom = 1026
	BottomRight = 1028
	BottomJustified = 1032
	BottomFlush = 1040
	BottomGeoAligned = 1056
	BaselineLeft = 2049
	Baseline = 2050
	BaselineRight = 2052
	BaselineJustified = 2056
	BaselineFlush = 2064
	BaselineGeoAligned = 2080
	MidlineLeft = 4097
	Midline = 4098
	MidlineRight = 4100
	MidlineJustified = 4104
	MidlineFlush = 4112
	MidlineGeoAligned = 4128
	CaplineLeft = 8193
	Capline = 8194
	CaplineRight = 8196
	CaplineJustified = 8200
	CaplineFlush = 8208
	CaplineGeoAligned = 8224


class ChangeText(BaseAction):

	@staticmethod
	def name():
		return 'ChangeText'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, font_asset=None, font_name=None, text=None, font_size=None, alignment=None, word_wrapping_ratios=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, font_asset, font_name, text, font_size, alignment, word_wrapping_ratios)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, font_asset=None, font_name=None, text=None, font_size=None, alignment=None, word_wrapping_ratios=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.font_asset = font_asset
		self.font_name = font_name
		self.text = text
		self.font_size = font_size
		self.alignment = alignment
		self.word_wrapping_ratios = word_wrapping_ratios
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.font_asset
		s += b'\x00' if self.font_asset is None else b'\x01'
		if self.font_asset is not None:
			s += self.font_asset.serialize()
		
		# serialize self.font_name
		s += b'\x00' if self.font_name is None else b'\x01'
		if self.font_name is not None:
			tmp75 = b''
			tmp75 += struct.pack('I', len(self.font_name))
			while len(tmp75) and tmp75[-1] == b'\x00'[0]:
				tmp75 = tmp75[:-1]
			s += struct.pack('B', len(tmp75))
			s += tmp75
			
			s += self.font_name.encode('ISO-8859-1') if PY3 else self.font_name
		
		# serialize self.text
		s += b'\x00' if self.text is None else b'\x01'
		if self.text is not None:
			tmp76 = b''
			tmp76 += struct.pack('I', len(self.text))
			while len(tmp76) and tmp76[-1] == b'\x00'[0]:
				tmp76 = tmp76[:-1]
			s += struct.pack('B', len(tmp76))
			s += tmp76
			
			s += self.text.encode('ISO-8859-1') if PY3 else self.text
		
		# serialize self.font_size
		s += b'\x00' if self.font_size is None else b'\x01'
		if self.font_size is not None:
			s += struct.pack('f', self.font_size)
		
		# serialize self.alignment
		s += b'\x00' if self.alignment is None else b'\x01'
		if self.alignment is not None:
			s += struct.pack('h', self.alignment.value)
		
		# serialize self.word_wrapping_ratios
		s += b'\x00' if self.word_wrapping_ratios is None else b'\x01'
		if self.word_wrapping_ratios is not None:
			s += struct.pack('f', self.word_wrapping_ratios)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.font_asset
		tmp77 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp77:
			self.font_asset = Asset()
			offset = self.font_asset.deserialize(s, offset)
		else:
			self.font_asset = None
		
		# deserialize self.font_name
		tmp78 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp78:
			tmp79 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp80 = s[offset:offset + tmp79]
			offset += tmp79
			tmp80 += b'\x00' * (4 - tmp79)
			tmp81 = struct.unpack('I', tmp80)[0]
			
			self.font_name = s[offset:offset + tmp81].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp81]
			offset += tmp81
		else:
			self.font_name = None
		
		# deserialize self.text
		tmp82 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp82:
			tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp84 = s[offset:offset + tmp83]
			offset += tmp83
			tmp84 += b'\x00' * (4 - tmp83)
			tmp85 = struct.unpack('I', tmp84)[0]
			
			self.text = s[offset:offset + tmp85].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp85]
			offset += tmp85
		else:
			self.text = None
		
		# deserialize self.font_size
		tmp86 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp86:
			self.font_size = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.font_size = None
		
		# deserialize self.alignment
		tmp87 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp87:
			tmp88 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
			self.alignment = ETextAlignmentOption(tmp88)
		else:
			self.alignment = None
		
		# deserialize self.word_wrapping_ratios
		tmp89 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp89:
			self.word_wrapping_ratios = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.word_wrapping_ratios = None
		
		return offset


class ESliderDirection(Enum):
	LeftToRight = 0
	RightToLeft = 1
	BottomToTop = 2
	TopToBottom = 3


class ChangeSlider(BaseAction):

	@staticmethod
	def name():
		return 'ChangeSlider'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, value=None, max_value=None, min_value=None, direction=None, background_color=None, fill_color=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, value, max_value, min_value, direction, background_color, fill_color)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, value=None, max_value=None, min_value=None, direction=None, background_color=None, fill_color=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.value = value
		self.max_value = max_value
		self.min_value = min_value
		self.direction = direction
		self.background_color = background_color
		self.fill_color = fill_color
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.value
		s += b'\x00' if self.value is None else b'\x01'
		if self.value is not None:
			s += struct.pack('f', self.value)
		
		# serialize self.max_value
		s += b'\x00' if self.max_value is None else b'\x01'
		if self.max_value is not None:
			s += struct.pack('f', self.max_value)
		
		# serialize self.min_value
		s += b'\x00' if self.min_value is None else b'\x01'
		if self.min_value is not None:
			s += struct.pack('f', self.min_value)
		
		# serialize self.direction
		s += b'\x00' if self.direction is None else b'\x01'
		if self.direction is not None:
			s += struct.pack('h', self.direction.value)
		
		# serialize self.background_color
		s += b'\x00' if self.background_color is None else b'\x01'
		if self.background_color is not None:
			s += self.background_color.serialize()
		
		# serialize self.fill_color
		s += b'\x00' if self.fill_color is None else b'\x01'
		if self.fill_color is not None:
			s += self.fill_color.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.value
		tmp90 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp90:
			self.value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.value = None
		
		# deserialize self.max_value
		tmp91 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp91:
			self.max_value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_value = None
		
		# deserialize self.min_value
		tmp92 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp92:
			self.min_value = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.min_value = None
		
		# deserialize self.direction
		tmp93 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp93:
			tmp94 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
			self.direction = ESliderDirection(tmp94)
		else:
			self.direction = None
		
		# deserialize self.background_color
		tmp95 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp95:
			self.background_color = Vector4()
			offset = self.background_color.deserialize(s, offset)
		else:
			self.background_color = None
		
		# deserialize self.fill_color
		tmp96 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp96:
			self.fill_color = Vector4()
			offset = self.fill_color.deserialize(s, offset)
		else:
			self.fill_color = None
		
		return offset


class ChangeRawImage(BaseAction):

	@staticmethod
	def name():
		return 'ChangeRawImage'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, texture_asset=None, material_asset=None, color=None, uv_rect=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, texture_asset, material_asset, color, uv_rect)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, texture_asset=None, material_asset=None, color=None, uv_rect=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.texture_asset = texture_asset
		self.material_asset = material_asset
		self.color = color
		self.uv_rect = uv_rect
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.texture_asset
		s += b'\x00' if self.texture_asset is None else b'\x01'
		if self.texture_asset is not None:
			s += self.texture_asset.serialize()
		
		# serialize self.material_asset
		s += b'\x00' if self.material_asset is None else b'\x01'
		if self.material_asset is not None:
			s += self.material_asset.serialize()
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.uv_rect
		s += b'\x00' if self.uv_rect is None else b'\x01'
		if self.uv_rect is not None:
			s += self.uv_rect.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.texture_asset
		tmp97 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp97:
			self.texture_asset = Asset()
			offset = self.texture_asset.deserialize(s, offset)
		else:
			self.texture_asset = None
		
		# deserialize self.material_asset
		tmp98 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp98:
			self.material_asset = Asset()
			offset = self.material_asset.deserialize(s, offset)
		else:
			self.material_asset = None
		
		# deserialize self.color
		tmp99 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp99:
			self.color = Vector4()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.uv_rect
		tmp100 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp100:
			self.uv_rect = Vector4()
			offset = self.uv_rect.deserialize(s, offset)
		else:
			self.uv_rect = None
		
		return offset


class ChangeSiblingOrder(BaseAction):

	@staticmethod
	def name():
		return 'ChangeSiblingOrder'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, new_index=None, goto_first=None, goto_last=None, change_index=None, sibling_ref_as_base_index=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, new_index, goto_first, goto_last, change_index, sibling_ref_as_base_index)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, new_index=None, goto_first=None, goto_last=None, change_index=None, sibling_ref_as_base_index=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.new_index = new_index
		self.goto_first = goto_first
		self.goto_last = goto_last
		self.change_index = change_index
		self.sibling_ref_as_base_index = sibling_ref_as_base_index
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.new_index
		s += b'\x00' if self.new_index is None else b'\x01'
		if self.new_index is not None:
			s += struct.pack('i', self.new_index)
		
		# serialize self.goto_first
		s += b'\x00' if self.goto_first is None else b'\x01'
		if self.goto_first is not None:
			s += struct.pack('?', self.goto_first)
		
		# serialize self.goto_last
		s += b'\x00' if self.goto_last is None else b'\x01'
		if self.goto_last is not None:
			s += struct.pack('?', self.goto_last)
		
		# serialize self.change_index
		s += b'\x00' if self.change_index is None else b'\x01'
		if self.change_index is not None:
			s += struct.pack('i', self.change_index)
		
		# serialize self.sibling_ref_as_base_index
		s += b'\x00' if self.sibling_ref_as_base_index is None else b'\x01'
		if self.sibling_ref_as_base_index is not None:
			tmp101 = b''
			tmp101 += struct.pack('I', len(self.sibling_ref_as_base_index))
			while len(tmp101) and tmp101[-1] == b'\x00'[0]:
				tmp101 = tmp101[:-1]
			s += struct.pack('B', len(tmp101))
			s += tmp101
			
			s += self.sibling_ref_as_base_index.encode('ISO-8859-1') if PY3 else self.sibling_ref_as_base_index
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.new_index
		tmp102 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp102:
			self.new_index = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.new_index = None
		
		# deserialize self.goto_first
		tmp103 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp103:
			self.goto_first = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.goto_first = None
		
		# deserialize self.goto_last
		tmp104 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp104:
			self.goto_last = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.goto_last = None
		
		# deserialize self.change_index
		tmp105 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp105:
			self.change_index = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.change_index = None
		
		# deserialize self.sibling_ref_as_base_index
		tmp106 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp106:
			tmp107 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp108 = s[offset:offset + tmp107]
			offset += tmp107
			tmp108 += b'\x00' * (4 - tmp107)
			tmp109 = struct.unpack('I', tmp108)[0]
			
			self.sibling_ref_as_base_index = s[offset:offset + tmp109].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp109]
			offset += tmp109
		else:
			self.sibling_ref_as_base_index = None
		
		return offset


class EComponentType(Enum):
	ParticleSystemManager = 0


class ManageComponents(BaseAction):

	@staticmethod
	def name():
		return 'ManageComponents'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, type=None, add=None, is_active=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, type, add, is_active)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, type=None, add=None, is_active=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.type = type
		self.add = add
		self.is_active = is_active
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			s += struct.pack('b', self.type.value)
		
		# serialize self.add
		s += b'\x00' if self.add is None else b'\x01'
		if self.add is not None:
			s += struct.pack('?', self.add)
		
		# serialize self.is_active
		s += b'\x00' if self.is_active is None else b'\x01'
		if self.is_active is not None:
			s += struct.pack('?', self.is_active)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.type
		tmp110 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp110:
			tmp111 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = EComponentType(tmp111)
		else:
			self.type = None
		
		# deserialize self.add
		tmp112 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp112:
			self.add = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.add = None
		
		# deserialize self.is_active
		tmp113 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp113:
			self.is_active = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_active = None
		
		return offset


class ChangeSprite(BaseAction):

	@staticmethod
	def name():
		return 'ChangeSprite'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, sprite_asset=None, color=None, flip_x=None, flip_y=None, order=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, sprite_asset, color, flip_x, flip_y, order)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, sprite_asset=None, color=None, flip_x=None, flip_y=None, order=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.sprite_asset = sprite_asset
		self.color = color
		self.flip_x = flip_x
		self.flip_y = flip_y
		self.order = order
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.sprite_asset
		s += b'\x00' if self.sprite_asset is None else b'\x01'
		if self.sprite_asset is not None:
			s += self.sprite_asset.serialize()
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.flip_x
		s += b'\x00' if self.flip_x is None else b'\x01'
		if self.flip_x is not None:
			s += struct.pack('?', self.flip_x)
		
		# serialize self.flip_y
		s += b'\x00' if self.flip_y is None else b'\x01'
		if self.flip_y is not None:
			s += struct.pack('?', self.flip_y)
		
		# serialize self.order
		s += b'\x00' if self.order is None else b'\x01'
		if self.order is not None:
			s += struct.pack('i', self.order)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.sprite_asset
		tmp114 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp114:
			self.sprite_asset = Asset()
			offset = self.sprite_asset.deserialize(s, offset)
		else:
			self.sprite_asset = None
		
		# deserialize self.color
		tmp115 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp115:
			self.color = Vector4()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.flip_x
		tmp116 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp116:
			self.flip_x = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.flip_x = None
		
		# deserialize self.flip_y
		tmp117 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp117:
			self.flip_y = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.flip_y = None
		
		# deserialize self.order
		tmp118 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp118:
			self.order = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.order = None
		
		return offset


class ChangeMaterial(BaseAction):

	@staticmethod
	def name():
		return 'ChangeMaterial'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, material_asset=None, index=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, material_asset, index)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, material_asset=None, index=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.material_asset = material_asset
		self.index = index
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.material_asset
		s += b'\x00' if self.material_asset is None else b'\x01'
		if self.material_asset is not None:
			s += self.material_asset.serialize()
		
		# serialize self.index
		s += b'\x00' if self.index is None else b'\x01'
		if self.index is not None:
			s += struct.pack('i', self.index)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.material_asset
		tmp119 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp119:
			self.material_asset = Asset()
			offset = self.material_asset.deserialize(s, offset)
		else:
			self.material_asset = None
		
		# deserialize self.index
		tmp120 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp120:
			self.index = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.index = None
		
		return offset


class ChangeEllipse2D(BaseAction):

	@staticmethod
	def name():
		return 'ChangeEllipse2D'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, fill_color=None, x_radius=None, y_radius=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, fill_color, x_radius, y_radius)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, fill_color=None, x_radius=None, y_radius=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.fill_color = fill_color
		self.x_radius = x_radius
		self.y_radius = y_radius
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.fill_color
		s += b'\x00' if self.fill_color is None else b'\x01'
		if self.fill_color is not None:
			s += self.fill_color.serialize()
		
		# serialize self.x_radius
		s += b'\x00' if self.x_radius is None else b'\x01'
		if self.x_radius is not None:
			s += struct.pack('f', self.x_radius)
		
		# serialize self.y_radius
		s += b'\x00' if self.y_radius is None else b'\x01'
		if self.y_radius is not None:
			s += struct.pack('f', self.y_radius)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.fill_color
		tmp121 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp121:
			self.fill_color = Vector4()
			offset = self.fill_color.deserialize(s, offset)
		else:
			self.fill_color = None
		
		# deserialize self.x_radius
		tmp122 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp122:
			self.x_radius = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x_radius = None
		
		# deserialize self.y_radius
		tmp123 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp123:
			self.y_radius = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y_radius = None
		
		return offset


class ChangePolygon2D(BaseAction):

	@staticmethod
	def name():
		return 'ChangePolygon2D'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, fill_color=None, vertices=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, fill_color, vertices)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, fill_color=None, vertices=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.fill_color = fill_color
		self.vertices = vertices
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.fill_color
		s += b'\x00' if self.fill_color is None else b'\x01'
		if self.fill_color is not None:
			s += self.fill_color.serialize()
		
		# serialize self.vertices
		s += b'\x00' if self.vertices is None else b'\x01'
		if self.vertices is not None:
			tmp124 = b''
			tmp124 += struct.pack('I', len(self.vertices))
			while len(tmp124) and tmp124[-1] == b'\x00'[0]:
				tmp124 = tmp124[:-1]
			s += struct.pack('B', len(tmp124))
			s += tmp124
			
			for tmp125 in self.vertices:
				s += b'\x00' if tmp125 is None else b'\x01'
				if tmp125 is not None:
					s += tmp125.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.fill_color
		tmp126 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp126:
			self.fill_color = Vector4()
			offset = self.fill_color.deserialize(s, offset)
		else:
			self.fill_color = None
		
		# deserialize self.vertices
		tmp127 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp127:
			tmp128 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp129 = s[offset:offset + tmp128]
			offset += tmp128
			tmp129 += b'\x00' * (4 - tmp128)
			tmp130 = struct.unpack('I', tmp129)[0]
			
			self.vertices = []
			for tmp131 in range(tmp130):
				tmp133 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp133:
					tmp132 = Vector2()
					offset = tmp132.deserialize(s, offset)
				else:
					tmp132 = None
				self.vertices.append(tmp132)
		else:
			self.vertices = None
		
		return offset


class ChangeLine(BaseAction):

	@staticmethod
	def name():
		return 'ChangeLine'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, fill_color=None, vertices=None, width=None, corner_vertices=None, end_cap_vertices=None, loop=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, fill_color, vertices, width, corner_vertices, end_cap_vertices, loop)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, fill_color=None, vertices=None, width=None, corner_vertices=None, end_cap_vertices=None, loop=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.fill_color = fill_color
		self.vertices = vertices
		self.width = width
		self.corner_vertices = corner_vertices
		self.end_cap_vertices = end_cap_vertices
		self.loop = loop
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.fill_color
		s += b'\x00' if self.fill_color is None else b'\x01'
		if self.fill_color is not None:
			s += self.fill_color.serialize()
		
		# serialize self.vertices
		s += b'\x00' if self.vertices is None else b'\x01'
		if self.vertices is not None:
			tmp134 = b''
			tmp134 += struct.pack('I', len(self.vertices))
			while len(tmp134) and tmp134[-1] == b'\x00'[0]:
				tmp134 = tmp134[:-1]
			s += struct.pack('B', len(tmp134))
			s += tmp134
			
			for tmp135 in self.vertices:
				s += b'\x00' if tmp135 is None else b'\x01'
				if tmp135 is not None:
					s += tmp135.serialize()
		
		# serialize self.width
		s += b'\x00' if self.width is None else b'\x01'
		if self.width is not None:
			s += struct.pack('f', self.width)
		
		# serialize self.corner_vertices
		s += b'\x00' if self.corner_vertices is None else b'\x01'
		if self.corner_vertices is not None:
			s += struct.pack('i', self.corner_vertices)
		
		# serialize self.end_cap_vertices
		s += b'\x00' if self.end_cap_vertices is None else b'\x01'
		if self.end_cap_vertices is not None:
			s += struct.pack('i', self.end_cap_vertices)
		
		# serialize self.loop
		s += b'\x00' if self.loop is None else b'\x01'
		if self.loop is not None:
			s += struct.pack('?', self.loop)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.fill_color
		tmp136 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp136:
			self.fill_color = Vector4()
			offset = self.fill_color.deserialize(s, offset)
		else:
			self.fill_color = None
		
		# deserialize self.vertices
		tmp137 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp137:
			tmp138 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp139 = s[offset:offset + tmp138]
			offset += tmp138
			tmp139 += b'\x00' * (4 - tmp138)
			tmp140 = struct.unpack('I', tmp139)[0]
			
			self.vertices = []
			for tmp141 in range(tmp140):
				tmp143 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp143:
					tmp142 = Vector2()
					offset = tmp142.deserialize(s, offset)
				else:
					tmp142 = None
				self.vertices.append(tmp142)
		else:
			self.vertices = None
		
		# deserialize self.width
		tmp144 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp144:
			self.width = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.corner_vertices
		tmp145 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp145:
			self.corner_vertices = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.corner_vertices = None
		
		# deserialize self.end_cap_vertices
		tmp146 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp146:
			self.end_cap_vertices = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.end_cap_vertices = None
		
		# deserialize self.loop
		tmp147 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp147:
			self.loop = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.loop = None
		
		return offset


class ELightType(Enum):
	Spot = 0
	Directional = 1
	Point = 2


class ELightShadowType(Enum):
	Disabled = 0
	Hard = 1
	Soft = 2


class ChangeLight(BaseAction):

	@staticmethod
	def name():
		return 'ChangeLight'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, type=None, range=None, spot_angle=None, color=None, intensity=None, indirect_multiplier=None, shadow_type=None, shadow_strength=None, shadow_bias=None, shadow_normal_bias=None, shadow_near_plane=None, cookie_asset=None, cookie_size=None, flare_asset=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, type, range, spot_angle, color, intensity, indirect_multiplier, shadow_type, shadow_strength, shadow_bias, shadow_normal_bias, shadow_near_plane, cookie_asset, cookie_size, flare_asset)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, type=None, range=None, spot_angle=None, color=None, intensity=None, indirect_multiplier=None, shadow_type=None, shadow_strength=None, shadow_bias=None, shadow_normal_bias=None, shadow_near_plane=None, cookie_asset=None, cookie_size=None, flare_asset=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.type = type
		self.range = range
		self.spot_angle = spot_angle
		self.color = color
		self.intensity = intensity
		self.indirect_multiplier = indirect_multiplier
		self.shadow_type = shadow_type
		self.shadow_strength = shadow_strength
		self.shadow_bias = shadow_bias
		self.shadow_normal_bias = shadow_normal_bias
		self.shadow_near_plane = shadow_near_plane
		self.cookie_asset = cookie_asset
		self.cookie_size = cookie_size
		self.flare_asset = flare_asset
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			s += struct.pack('b', self.type.value)
		
		# serialize self.range
		s += b'\x00' if self.range is None else b'\x01'
		if self.range is not None:
			s += struct.pack('f', self.range)
		
		# serialize self.spot_angle
		s += b'\x00' if self.spot_angle is None else b'\x01'
		if self.spot_angle is not None:
			s += struct.pack('f', self.spot_angle)
		
		# serialize self.color
		s += b'\x00' if self.color is None else b'\x01'
		if self.color is not None:
			s += self.color.serialize()
		
		# serialize self.intensity
		s += b'\x00' if self.intensity is None else b'\x01'
		if self.intensity is not None:
			s += struct.pack('f', self.intensity)
		
		# serialize self.indirect_multiplier
		s += b'\x00' if self.indirect_multiplier is None else b'\x01'
		if self.indirect_multiplier is not None:
			s += struct.pack('f', self.indirect_multiplier)
		
		# serialize self.shadow_type
		s += b'\x00' if self.shadow_type is None else b'\x01'
		if self.shadow_type is not None:
			s += struct.pack('b', self.shadow_type.value)
		
		# serialize self.shadow_strength
		s += b'\x00' if self.shadow_strength is None else b'\x01'
		if self.shadow_strength is not None:
			s += struct.pack('f', self.shadow_strength)
		
		# serialize self.shadow_bias
		s += b'\x00' if self.shadow_bias is None else b'\x01'
		if self.shadow_bias is not None:
			s += struct.pack('f', self.shadow_bias)
		
		# serialize self.shadow_normal_bias
		s += b'\x00' if self.shadow_normal_bias is None else b'\x01'
		if self.shadow_normal_bias is not None:
			s += struct.pack('f', self.shadow_normal_bias)
		
		# serialize self.shadow_near_plane
		s += b'\x00' if self.shadow_near_plane is None else b'\x01'
		if self.shadow_near_plane is not None:
			s += struct.pack('f', self.shadow_near_plane)
		
		# serialize self.cookie_asset
		s += b'\x00' if self.cookie_asset is None else b'\x01'
		if self.cookie_asset is not None:
			s += self.cookie_asset.serialize()
		
		# serialize self.cookie_size
		s += b'\x00' if self.cookie_size is None else b'\x01'
		if self.cookie_size is not None:
			s += struct.pack('f', self.cookie_size)
		
		# serialize self.flare_asset
		s += b'\x00' if self.flare_asset is None else b'\x01'
		if self.flare_asset is not None:
			s += self.flare_asset.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.type
		tmp148 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp148:
			tmp149 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = ELightType(tmp149)
		else:
			self.type = None
		
		# deserialize self.range
		tmp150 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp150:
			self.range = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.range = None
		
		# deserialize self.spot_angle
		tmp151 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp151:
			self.spot_angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.spot_angle = None
		
		# deserialize self.color
		tmp152 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp152:
			self.color = Vector4()
			offset = self.color.deserialize(s, offset)
		else:
			self.color = None
		
		# deserialize self.intensity
		tmp153 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp153:
			self.intensity = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.intensity = None
		
		# deserialize self.indirect_multiplier
		tmp154 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp154:
			self.indirect_multiplier = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.indirect_multiplier = None
		
		# deserialize self.shadow_type
		tmp155 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp155:
			tmp156 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.shadow_type = ELightShadowType(tmp156)
		else:
			self.shadow_type = None
		
		# deserialize self.shadow_strength
		tmp157 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp157:
			self.shadow_strength = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.shadow_strength = None
		
		# deserialize self.shadow_bias
		tmp158 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp158:
			self.shadow_bias = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.shadow_bias = None
		
		# deserialize self.shadow_normal_bias
		tmp159 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp159:
			self.shadow_normal_bias = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.shadow_normal_bias = None
		
		# deserialize self.shadow_near_plane
		tmp160 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp160:
			self.shadow_near_plane = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.shadow_near_plane = None
		
		# deserialize self.cookie_asset
		tmp161 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp161:
			self.cookie_asset = Asset()
			offset = self.cookie_asset.deserialize(s, offset)
		else:
			self.cookie_asset = None
		
		# deserialize self.cookie_size
		tmp162 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp162:
			self.cookie_size = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.cookie_size = None
		
		# deserialize self.flare_asset
		tmp163 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp163:
			self.flare_asset = Asset()
			offset = self.flare_asset.deserialize(s, offset)
		else:
			self.flare_asset = None
		
		return offset


class ECameraClearFlag(Enum):
	Skybox = 1
	SolidColor = 2
	Depth = 3
	Nothing = 4


class ChangeCamera(BaseAction):

	@staticmethod
	def name():
		return 'ChangeCamera'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, clear_flag=None, background_color=None, is_orthographic=None, orthographic_size=None, field_of_view=None, near_clip_plane=None, far_clip_plane=None):
		self.initialize(cycle, ref, child_ref, duration_cycles, clear_flag, background_color, is_orthographic, orthographic_size, field_of_view, near_clip_plane, far_clip_plane)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None, clear_flag=None, background_color=None, is_orthographic=None, orthographic_size=None, field_of_view=None, near_clip_plane=None, far_clip_plane=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
		
		self.clear_flag = clear_flag
		self.background_color = background_color
		self.is_orthographic = is_orthographic
		self.orthographic_size = orthographic_size
		self.field_of_view = field_of_view
		self.near_clip_plane = near_clip_plane
		self.far_clip_plane = far_clip_plane
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		# serialize self.clear_flag
		s += b'\x00' if self.clear_flag is None else b'\x01'
		if self.clear_flag is not None:
			s += struct.pack('b', self.clear_flag.value)
		
		# serialize self.background_color
		s += b'\x00' if self.background_color is None else b'\x01'
		if self.background_color is not None:
			s += self.background_color.serialize()
		
		# serialize self.is_orthographic
		s += b'\x00' if self.is_orthographic is None else b'\x01'
		if self.is_orthographic is not None:
			s += struct.pack('?', self.is_orthographic)
		
		# serialize self.orthographic_size
		s += b'\x00' if self.orthographic_size is None else b'\x01'
		if self.orthographic_size is not None:
			s += struct.pack('f', self.orthographic_size)
		
		# serialize self.field_of_view
		s += b'\x00' if self.field_of_view is None else b'\x01'
		if self.field_of_view is not None:
			s += struct.pack('f', self.field_of_view)
		
		# serialize self.near_clip_plane
		s += b'\x00' if self.near_clip_plane is None else b'\x01'
		if self.near_clip_plane is not None:
			s += struct.pack('f', self.near_clip_plane)
		
		# serialize self.far_clip_plane
		s += b'\x00' if self.far_clip_plane is None else b'\x01'
		if self.far_clip_plane is not None:
			s += struct.pack('f', self.far_clip_plane)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		# deserialize self.clear_flag
		tmp164 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp164:
			tmp165 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.clear_flag = ECameraClearFlag(tmp165)
		else:
			self.clear_flag = None
		
		# deserialize self.background_color
		tmp166 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp166:
			self.background_color = Vector4()
			offset = self.background_color.deserialize(s, offset)
		else:
			self.background_color = None
		
		# deserialize self.is_orthographic
		tmp167 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp167:
			self.is_orthographic = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_orthographic = None
		
		# deserialize self.orthographic_size
		tmp168 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp168:
			self.orthographic_size = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.orthographic_size = None
		
		# deserialize self.field_of_view
		tmp169 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp169:
			self.field_of_view = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.field_of_view = None
		
		# deserialize self.near_clip_plane
		tmp170 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp170:
			self.near_clip_plane = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.near_clip_plane = None
		
		# deserialize self.far_clip_plane
		tmp171 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp171:
			self.far_clip_plane = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.far_clip_plane = None
		
		return offset


class StoreBundleData(object):

	@staticmethod
	def name():
		return 'StoreBundleData'


	def __init__(self, bundle_name=None, bundle_data=None):
		self.initialize(bundle_name, bundle_data)
	

	def initialize(self, bundle_name=None, bundle_data=None):
		self.bundle_name = bundle_name
		self.bundle_data = bundle_data
	

	def serialize(self):
		s = b''
		
		# serialize self.bundle_name
		s += b'\x00' if self.bundle_name is None else b'\x01'
		if self.bundle_name is not None:
			tmp172 = b''
			tmp172 += struct.pack('I', len(self.bundle_name))
			while len(tmp172) and tmp172[-1] == b'\x00'[0]:
				tmp172 = tmp172[:-1]
			s += struct.pack('B', len(tmp172))
			s += tmp172
			
			s += self.bundle_name.encode('ISO-8859-1') if PY3 else self.bundle_name
		
		# serialize self.bundle_data
		s += b'\x00' if self.bundle_data is None else b'\x01'
		if self.bundle_data is not None:
			tmp173 = b''
			tmp173 += struct.pack('I', len(self.bundle_data))
			while len(tmp173) and tmp173[-1] == b'\x00'[0]:
				tmp173 = tmp173[:-1]
			s += struct.pack('B', len(tmp173))
			s += tmp173
			
			s += self.bundle_data.encode('ISO-8859-1') if PY3 else self.bundle_data
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.bundle_name
		tmp174 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp174:
			tmp175 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp176 = s[offset:offset + tmp175]
			offset += tmp175
			tmp176 += b'\x00' * (4 - tmp175)
			tmp177 = struct.unpack('I', tmp176)[0]
			
			self.bundle_name = s[offset:offset + tmp177].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp177]
			offset += tmp177
		else:
			self.bundle_name = None
		
		# deserialize self.bundle_data
		tmp178 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp178:
			tmp179 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp180 = s[offset:offset + tmp179]
			offset += tmp179
			tmp180 += b'\x00' * (4 - tmp179)
			tmp181 = struct.unpack('I', tmp180)[0]
			
			self.bundle_data = s[offset:offset + tmp181].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp181]
			offset += tmp181
		else:
			self.bundle_data = None
		
		return offset


class ClearScene(BaseAction):

	@staticmethod
	def name():
		return 'ClearScene'


	def __init__(self, cycle=None, ref=None, child_ref=None, duration_cycles=None):
		self.initialize(cycle, ref, child_ref, duration_cycles)
	

	def initialize(self, cycle=None, ref=None, child_ref=None, duration_cycles=None):
		BaseAction.initialize(self, cycle, ref, child_ref, duration_cycles)
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += BaseAction.serialize(self)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = BaseAction.deserialize(self, s, offset)
		
		return offset


class EndCycle(object):

	@staticmethod
	def name():
		return 'EndCycle'


	def __init__(self):
		self.initialize()
	

	def initialize(self):
		pass
	

	def serialize(self):
		s = b''
		
		return s
	

	def deserialize(self, s, offset=0):
		return offset