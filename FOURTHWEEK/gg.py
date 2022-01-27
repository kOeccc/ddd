mobile_devices = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
    'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
}

home_devices = {
    'cucuLot': 2011,
    'cucuBlock': 2010,
    'cucuWall': 2010,
    'cucuMonitor': 2020,
    'cucuLamp': 2015,
    'cucuTable': 2016,
    'cucuTV': 2017,
}

not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}

result_supported = {}


# Функция объединяет ключи двух словарей в один set и возвращает его
def union_devices(devices_obj_1, devices_obj_2):
    union_set = set(devices_obj_1).union(devices_obj_2)
    return union_set


# Функция находит разницу двух сетов и возвращает её в виде set
def difference_device(all_devices, not_supported_devices):
    diff_set = set(all_devices).difference(not_supported_devices)
    return diff_set


# Функция копирует элементы из исходных словарей в результирующий словарь
def is_supported(dict_devices, device):
    if device in dict_devices:
        result_supported[device] = dict_devices[device]


# Вызываем union_devices(), чтобы получить полный перечень устройств
all_devices = union_devices(mobile_devices, home_devices)

# В result_devices сохранить сет, который вернёт функция difference_device()
result_devices = difference_device(all_devices, not_supported_devices)

# Перебрать в цикле сет result_devices и для каждого элемента
# дважды вызвать функцию is_supported:
# - с аргументами mobile_devices, device
# - и с аргументами home_devices, device
for device in result_devices:
    is_supported(mobile_devices, device)
    is_supported(home_devices, device)
    # Тут второй вызов


print(result_supported)
