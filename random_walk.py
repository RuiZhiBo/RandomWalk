from random import choice

class RandomWalk:
	"""一个随机数生成器"""

	def __init__(self, num_points=5000):
		"""初始化随机数的属性"""
		self.num_points = num_points

		#初始化随机漫步为零
		self.x_values = [0]
		self.y_valuse = [0]

	def fill_walk(self):
		while len(self.x_values) < self.num_points:
			"""计算随机漫步的所有点"""
			x_dirction = choice([1, -1])
			x_distance = choice([0, 1, 2, 3, 4])
			x_step = x_dirction * x_distance

			y_dirction = choice([1, -1])
			y_distance = choice([0, 1, 2, 3, 4])
			y_step = y_dirction * y_distance

			#禁止停留原地
			if x_step == 0 and y_step == 0:
				continue

			#计算下一个点
			x = self.x_values[-1] + x_step
			y = self.y_valuse[-1] + y_step

			self.x_values.append(x)
			self.y_valuse.append(y)
