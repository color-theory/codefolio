import { validateParens } from "./ValidParens";

describe("validateParens", () => {
  it("should return true when s = '()'", () => {
    const s = "()";
    expect(validateParens(s)).toEqual(true);
  });

  it("should return true when s = '()[]{}'", () => {
    const s = "()[]{}";
    expect(validateParens(s)).toEqual(true);
  });

  it("should return false when s = '(]'", () => {
    const s = "(]";
    expect(validateParens(s)).toEqual(false);
  });

  it("should return false when s = '([)]'", () => {
    const s = "([)]";
    expect(validateParens(s)).toEqual(false);
  });

  it("should return true when s = '{[]}'", () => {
    const s = "{[]}";
    expect(validateParens(s)).toEqual(true);
  });

  it("should return false when s = '}'", () => {
    const s = "}";
    expect(validateParens(s)).toEqual(false);
  });

  it("should return false when s = '{hi}'", () => {
    const s = "{hi}";
    expect(validateParens(s)).toEqual(false);
  });

  it("should return true when s = ''", () => {
    const s = "";
    expect(validateParens(s)).toEqual(true);
  });
});
