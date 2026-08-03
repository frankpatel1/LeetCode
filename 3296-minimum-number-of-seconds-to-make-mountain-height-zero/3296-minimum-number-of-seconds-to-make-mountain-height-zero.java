class Solution {

    public long minNumberOfSeconds(int mountainHeight, int[] workerTimes) {
        long left = 1;
        long right = (long) 1e16;

        while (left < right) {
            long mid = left + (right - left) / 2;

            if (canFinish(mid, mountainHeight, workerTimes)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private boolean canFinish(long time, int mountainHeight, int[] workerTimes) {
        long total = 0;

        for (int w : workerTimes) {
            long height = (long) (Math.sqrt((2.0 * time) / w + 0.25) - 0.5);
            total += height;

            if (total >= mountainHeight) {
                return true;
            }
        }

        return false;
    }
}