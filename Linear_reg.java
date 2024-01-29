class LinearRegression {
    // Function to perform linear regression
    public static void linearRegression(int[] x, int[] y, int n) {
        // Calculate mean of x and y
        int sumX = 0, sumY = 0;
        for (int i = 0; i < n; i++) {
            sumX += x[i];
            sumY += y[i];
        }
        float meanX = (float) sumX / n;
        float meanY = (float) sumY / n;

        // Calculate slope (m) and intercept (b)
        float num = 0, den = 0;
        for (int i = 0; i < n; i++) {
            num += (x[i] - meanX) * (y[i] - meanY);
            den += (x[i] - meanX) * (x[i] - meanX);
        }
        float slope = num / den;
        float intercept = meanY - slope * meanX;

        // Display the equation
        System.out.printf("Linear Regression Equation: y = %.2fx + %.2f%n", slope, intercept);
    }

    public static void main(String[] args) {
        // Sample data
        int[] x = {1, 2, 3, 4, 5};
        int[] y = {2, 4, 5, 4, 5};
        int n = x.length;

        // Perform linear regression
        linearRegression(x, y, n);
    }
}
