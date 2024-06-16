int subtractProductAndSum(int n) {
    int product = 1;
    int sum = 0;
    while(n > 0){
        int rem =  n % 10;
        int num = n / 10;
        product *= rem;
        sum += rem;
        n = num;
    }
    return product - sum;
} 
