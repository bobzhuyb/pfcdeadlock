class TTLTag():
    def __init__(self, switch_name):
        self.name = switch_name
        self.ports = {}             # remote_switch:port_index
        self.ports[""] = 0          # reserved for local
        self.tagged_ports = {}      # (remote_switch, tag):1

    def add_port(self, remote_switch):
        self.ports[remote_switch] = len(self.ports)

    def register_port_tag(self, remote_switch, tag):
        self.tagged_ports[(remote_switch, tag)] = 1

    def get_new_tag(self, current_tag, last_hop, next_hop):
        return current_tag - 1

    def get_all_tagged_ports(self):
        r = [0] * len(self.tagged_ports.keys())
        index = 0
        for each in self.tagged_ports:
            r[index] = (self.name, self.ports[each[0]], each[1])
            index += 1
        return r

    # next_hop is the next switch class
    def is_port_dependency(self, port_index, current_tag, next_hop, next_port_index, next_tag):
        if next_hop.name not in self.ports:
            return False
        if self.name not in next_hop.ports:
            return False
        if next_hop.ports[self.name] != next_port_index:
            return False
        if current_tag != next_tag + 1:
            return False
        return True


class ClosTag(TTLTag):

    def get_new_tag(self, current_tag, last_hop, next_hop):
        if "empty" not in self.ports:
            return current_tag
        if last_hop not in self.ports:
            return current_tag
        if self.ports[last_hop] > self.ports["empty"] and self.ports[next_hop] > self.ports["empty"]:
            return current_tag - 1
        else:
            return current_tag
