class F1Score:
    def __init__(self):
        self.tp = 0
        self.fp = 0
        self.fn = 0

    def update(self, pred, target):
        pred = frozenset(x for x in pred)
        target = frozenset(x for x in target)
        self.tp += len(pred & target)
        self.fp += len(pred - target)
        self.fn += len(target - pred)

    def reset(self):
        self.tp = 0
        self.fp = 0
        self.fn = 0

    def get(self):
        if self.tp == 0:
            return 0.0
        precision = self.tp / (self.tp + self.fp)
        recall = self.tp / (self.tp + self.fn)
        return 2 / (1 / precision + 1 / recall)
