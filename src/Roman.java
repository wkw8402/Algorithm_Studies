import java.util.HashMap;

public class Roman {
        public int romanToInt(String s) {
                int i = 0;
                int integer = 0;
                HashMap<Character, Integer> rToI = makeConversion();
                HashMap<String, Integer> special = makeSpecial();
                while (i < s.length()) {
                        if (i == s.length() - 1) {
                                integer += rToI.get(s.charAt(i));
                                i++;
                        } else if (special.keySet().contains("" + s.charAt(i) + s.charAt(i + 1))) {
                                integer += special.get("" + s.charAt(i) + s.charAt(i + 1));
                                i += 2;
                        } else {
                                integer += rToI.get(s.charAt(i));
                                i++;
                        }
                }
                return integer;
        }

        private HashMap<Character, Integer> makeConversion() {
                HashMap<Character, Integer> rToI = new HashMap<>();
                rToI.put('I', 1);
                rToI.put('V', 5);
                rToI.put('X', 10);
                rToI.put('L', 50);
                rToI.put('C', 100);
                rToI.put('D', 500);
                rToI.put('M', 1000);
                return rToI;
        }

        private HashMap<String, Integer> makeSpecial() {
                HashMap<String, Integer> special = new HashMap<>();
                special.put("IV", 4);
                special.put("IX", 9);
                special.put("XL", 40);
                special.put("XC", 90);
                special.put("CD", 400);
                special.put("CM", 900);
                return special;
        }
}
