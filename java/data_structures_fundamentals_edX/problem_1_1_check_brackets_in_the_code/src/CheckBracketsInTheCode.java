public class CheckBracketsInTheCode {
    public static void main(String[] args) {
        String code_to_check = "foo()[](bar[i);";
        System.out.println(check_brackets(code_to_check));
    }

    public static String check_brackets(String string_of_code) {
        char stack[];
        int missing_bracket_place_no = 0;
        for  (int i : stack) {
            missing_bracket_place_no++;
            if (i in '([{') {
                stack.append(char);
            } else {
                if (i not in ')]}') {
                    continue;
                };
                if len(stack) == 0 {
                    return missing_bracket_place_no;
                };
                top = stack.pop();
                if (top == '[' && char != ']') || (top == '(' && char != ')') || (top == '{' && char != '}') {
                    return missing_bracket_place_no;
                }
            }
        }
        return "Success";
    }
}
