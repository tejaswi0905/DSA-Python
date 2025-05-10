import java.util.*;

class PathFinding {

    static class Node implements Comparable<Node> {
        int timeTaken;
        int remainingEnergy;
        int currentRow;
        int currentCol;

        Node(int timeTaken, int remainingEnergy, int currentRow, int currentCol) {
            this.timeTaken = timeTaken;
            this.remainingEnergy = remainingEnergy;
            this.currentRow = currentRow;
            this.currentCol = currentCol;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.timeTaken, other.timeTaken);
        }
    }

    public static String findPath(int rowCount, int colCount, String[][] grid, int[][] travelCost, int initialEnergy) {
        int[] startPos = null;
        int[] endPos = null;

        for (int i = 0; i < rowCount; i++) {
            for (int j = 0; j < colCount; j++) {
                if (grid[i][j].equals("S")) {
                    startPos = new int[]{i, j};
                    grid[i][j] = "0";
                } else if (grid[i][j].equals("D")) {
                    endPos = new int[]{i, j};
                    grid[i][j] = "0";
                }
            }
        }

        if (startPos == null || endPos == null) {
            return "Not Possible";
        }

        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.offer(new Node(0, initialEnergy, startPos[0], startPos[1]));

        int[][] minTime = new int[rowCount][colCount];
        int[][] maxEnergy = new int[rowCount][colCount];
        for (int[] row : minTime) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        for (int[] row : maxEnergy) {
            Arrays.fill(row, Integer.MIN_VALUE);
        }

        minTime[startPos[0]][startPos[1]] = 0;
        maxEnergy[startPos[0]][startPos[1]] = initialEnergy;

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!queue.isEmpty()) {
            Node current = queue.poll();

            if (current.currentRow == endPos[0] && current.currentCol == endPos[1]) {
                return current.timeTaken + " " + current.remainingEnergy;
            }

            for (int[] direction : directions) {
                int newRow = current.currentRow + direction[0];
                int newCol = current.currentCol + direction[1];

                if (newRow >= 0 && newRow < rowCount && newCol >= 0 && newCol < colCount) {
                    int hazard = Integer.parseInt(grid[newRow][newCol]);
                    int updatedEnergy = current.remainingEnergy - 1 - hazard;
                    int updatedTime = current.timeTaken + travelCost[newRow][newCol];

                    if (updatedEnergy >= 0 && (updatedTime < minTime[newRow][newCol] || updatedEnergy > maxEnergy[newRow][newCol])) {
                        minTime[newRow][newCol] = updatedTime;
                        maxEnergy[newRow][newCol] = updatedEnergy;
                        queue.offer(new Node(updatedTime, updatedEnergy, newRow, newCol));
                    }
                }
            }
        }

        return "Not Possible";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int rowCount = scanner.nextInt();
        int colCount = scanner.nextInt();
        scanner.nextLine();

        String[][] grid = new String[rowCount][colCount];
        for (int i = 0; i < rowCount; i++) {
            grid[i] = scanner.nextLine().split(" ");
        }

        int[][] travelCost = new int[rowCount][colCount];
        for (int i = 0; i < rowCount; i++) {
            for (int j = 0; j < colCount; j++) {
                travelCost[i][j] = scanner.nextInt();
            }
        }

        int initialEnergy = scanner.nextInt();

        System.out.print(findPath(rowCount, colCount, grid, travelCost, initialEnergy));
    }
}
