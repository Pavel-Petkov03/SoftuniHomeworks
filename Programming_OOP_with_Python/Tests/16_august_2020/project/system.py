from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        obj = PowerHardware(name, capacity, memory)
        System._hardware.append(obj)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        obj = HeavyHardware(name, capacity, memory)
        System._hardware.append(obj)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hard = [h for h in System._hardware if h.name == hardware_name]
        new_software_instance = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            obj = hard[0]
            obj.install(new_software_instance)
            System._software.append(new_software_instance)
        except IndexError:
            return "Hardware does not exist"
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hard = [h for h in System._hardware if h.name == hardware_name]

        new_software_instance = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            obj = hard[0]
            obj.install(new_software_instance)
            System._software.append(new_software_instance)
        except IndexError:
            return "Hardware does not exist"
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [h for h in System._software if h.name == software_name]
        if not hardware or not software:
            return "Some of the components do not exist"
        System._software.remove(software[0])
        hardware[0].uninstall(software[0])

    @staticmethod
    def analyze():
        result = [
            'System Analysis',
            f'Hardware Components: {len(System._hardware)}',
            f'Software Components: {len(System._software)}',
            f'Total Operational Memory: {int(sum([h.total_used_memory for h in System._hardware]))} / {int(sum([h.memory for h in System._hardware]))}',
            f'Total Capacity Taken: {int(sum([h.total_used_capacity for h in System._hardware]))} / {int(sum([h.capacity for h in System._hardware]))}'
        ]
        return "\n".join(result)

    @staticmethod
    def system_split():
        result = []
        for h in System._hardware:
            if len(h.software_components) == 0:
                a = None
            else:
                a = ", ".join([str(s) for s in h.software_components])
            result.append([
                f'Hardware Component - {h.name}',
                f'Express Software Components: {len([s for s in h.software_components if isinstance(s, ExpressSoftware)])}',
                f'Light Software Components: {len([s for s in h.software_components if isinstance(s, LightSoftware)])}',
                f'Memory Usage: {int(h.total_used_memory)} / {int(h.memory)}',
                f'Capacity Usage: {int(h.total_used_capacity)} / {int(h.capacity)}',
                f'Type: {h.type}',
                f'Software Components: {a}'
            ])
        result = "\n".join([j for l in result for j in l])
        return result
