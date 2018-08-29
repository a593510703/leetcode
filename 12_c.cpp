class Solution {
public:
    string OK(int &num){

        if (num / 1000 > 0) {
            num -= 1000;
            return "M";
        }

        if (num / 900 > 0) {
            num -= 900;
            return "CM";
        }
        if (num / 500 > 0) {
            num -= 500;
            return "D";
        }
        if (num / 400 > 0){
            num -= 400;
            return "CD";
        }
        if (num / 100 > 0){
            num -= 100;
            return "C";
        }
        if (num / 90 > 0){
            num -= 90;
            return "XC";
        }
        if (num / 50 > 0){
            num -= 50;
            return "L";
        }
        if (num / 40 > 0){
            num -= 40;
            return "XL";
        }
        if (num / 10 > 0){
            num -= 10;
            return "X";
        }
        if (num / 9 > 0){
            num -= 9;
            return "IX";
        }
        if (num / 5 > 0){
            num -= 5;
            return "V";
        }
        if (num / 4 > 0){
            num -= 4;
            return "IV";
        }
        num --;
        return "I";
    }
    string intToRoman(int num) {
        string str;
        while(num > 0){
            str += OK(num);
    }
    return str;
    }
};
