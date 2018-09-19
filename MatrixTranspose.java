import java.util.Scanner;

public class MatrixTranspose {
    private int[][] matrix;

    MatrixTranspose(int rows, int cols) {
        matrix = new int[rows][cols];
    }

    int[][] getMatrix() {
        return matrix;
    }

    int[][] transpose() {
        int[][] transposed = new int[matrix[0].length][matrix.length];

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                transposed[j][i] = matrix[i][j];
            }
        }


        return transposed;
    }

    static String visualize(int[][] mat) {
        StringBuilder output = new StringBuilder();

        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; j++) {
                output.append(mat[i][j]).append(" ");
            }

            output.append("\n");
        }

        return output.toString();
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        MatrixTranspose matrixTranspose = new MatrixTranspose(kb.nextInt(), kb.nextInt());
        int[][] matrix = matrixTranspose.getMatrix();

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                matrix[i][j] = kb.nextInt();
            }
        }

        System.out.println(visualize(matrixTranspose.transpose()));
    }
}
