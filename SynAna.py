class SyntacticalAnalyser(object):

    rules = {}
    result = []

    data = []

    def __init__(self, rules):
        self.rules = rules

    def check(self,rule, data):
        # if the data length is longer than the rule length return false
        if self.rules[rule].len() < data.len():
            return False
        else:
            #browsing the data
            for count, element in enumerate(data):
                # if the element doesn't share the same type or the value is set and not the same return false
                if element[0] != self.rules[rule][count][0] or\
                   (element[1] != "" and element[1] != self.rules[rule][count][1]):
                        return False
            # at this point all the elements on data are in the rule
            # if they share the same length than this is a full match
            if data.len() == self.rules[rule].len():
                return {
                    "type": "full",
                    "recursive": False,
                    "rule": "",
                    "next": ""
                }
            # else they have a partial match
            else:
                return {
                    "type": "partial",
                    "recursive": False,
                    "rule": "",
                    "next": self.rules[rule][count + 1]
                }


    def match(self, data):
        found = False
        exp_next = []
        for rule in self.rules:
            # check if this data matches any rule
            result = self.check(rule, data)

            # if so
            if result:
                found = True
                if result["type"] == "full":
                    return {
                        "action": 2,
                        "expect_next": [],
                        "expect_rule": "",
                        "matched_rule": rule
                    }
                else:
                    if result["recursive"]:
                        return {
                            "action": 3,
                            "expect_next": [],
                            "expect_rule": result['rule'],
                            "matched_rules": ""
                        }
                    else:
                        exp_next.append(result['next'])

        # if not return empty arrays and code 0 which means no rule found
        if not found:
            return {
                "action": 0,
                "expect_next": [],
                "expect_rule": "",
                "matched_rule": ""
            }
        else:
            return {
                "action": 1,
                "expect_next": exp_next,
                "expect_rule": "",
                "matched_rule": ""
            }

    def parse(self, data, expect_rule = None):

        # temporary elements chain
        temp_chain = []
        expect_next = ()

        for pattern, value in data:
            # testing if we are expecting a certain element/s
            if expect_next is not None:
                # if so then test if the pattern is not correct and the value doesn't match
                for expect in expect_next:
                    if pattern != expect[0] or (expect_next[1] != "" and expect[1] != value):
                        raise Exception("unexpected " + value)

            # if none of that goes than add this element to the chain
            temp_chain.append((pattern, value))
            # remove the element from the
            data.pop(0)

            # matching the result
            match_result = self.match(temp_chain)

            # list of expected elements next
            expect_next = match_result["expect_next"]
            # this var stocks the action to take
            action = match_result["action"]
            # in case of recursive cal required this is the name of the rule its supposed to find
            exp_rule = match_result["expect_rule"]
            # in case a full match found with a rule this hold the name of the rule
            rule = match_result["matched_rule"]

            # processing the outcome of the match
            # 0 means no match rule found
            if action == 0:
                raise Exception("syntax error! at " + value)

            # 1 means at least one rule was found
            elif action == 1:
                pass

            # 2 means a rule was found and it was complete
            elif action == 2:
                # if no rule is expected ( not in recursive call)
                if expect_rule == None:
                    self.result.append((temp_chain, rule))
                else:
                    # if the result matches the expected rule
                    if self.check(expect_next, temp_chain):
                        # save the data and return the result
                        self.data = data
                        return temp_chain
                    else:
                        raise Exception("Syntax error!")
            # 3 means a recursive call with a certain rule to expect
            elif action == 3:
                self.result.append((self.parse(data, exp_rule), exp_rule))
                data = self.data

        return self.result
