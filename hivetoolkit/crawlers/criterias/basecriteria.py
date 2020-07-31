from ...utils import arguments


class BaseCriteria:
    RULES = {"empty_rule": {"type": list, "sub_type": str}}

    def __init__(self, config_path=None):
        self.__rules = dict()
        # TODO: implement config loading
        pass

    def set_rule(self, rule_name, value):
        if not rule_name in self.RULES.keys():
            raise NotImplementedError(f"The rule '{rule_name}' doesn't exists.")

        # unpack rule
        rule = self.RULES[rule_name]
        try:
            arguments.check_arg(
                value,
                rule["type"],
                f"value (for {rule_name})",
                sub_type=rule.get("sub_type", None),
            )
        except TypeError as e:
            raise TypeError(e) from e
        else:
            self._add_rule(rule_name, value)

    def reset(self):
        self.__rules = dict()

    def _add_rule(self, rule_name, value):
        self.__rules[rule_name] = value

    @property
    def rules(self):
        return self.__rules

    @property
    def rules_names(self):
        return list(self.rules.keys())


class ConfigHandler:
    pass
