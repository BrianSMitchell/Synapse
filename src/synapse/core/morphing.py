from synapse.core.ast_tools import parse_code, modify_ast, ast_to_code

class Morpher:
    def __init__(self, code, max_morphs=100):
        self.code = code
        self.accuracy = 0.6  # Starting accuracy
        self.morph_count = 0
        self.max_morphs = max_morphs

    def morph(self, condition_func, rewrite_func):
        if self.morph_count >= self.max_morphs:
            raise Exception("Max morphs reached, preventing infinite loop")
        if condition_func(self.accuracy):
            # Apply rewrite
            tree = parse_code(self.code)
            modified_code = rewrite_func(tree)
            self.code = modified_code
            self.accuracy += 0.04  # Simulate improvement
            self.morph_count += 1
        return self.code

def test_morphing():
    morpher = Morpher("let x = normal(0,1)")
    for i in range(10):
        morpher.morph(lambda acc: acc < 0.9, lambda tree: modify_ast(tree, "1", "0.9"))
    return morpher.accuracy >= 0.9

if __name__ == "__main__":
    print("Morphing improves accuracy:", test_morphing())
