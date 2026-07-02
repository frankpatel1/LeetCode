class Solution:
    def maxBalancedShipments(self, weight: list[int]) -> int:
        result = 0
        mx = 0
        
        for x in weight:
            if x < mx:
                # We found a valid balanced shipment segment ending at x!
                result += 1
                # Reset max tracker for the next new shipment segment
                mx = 0
            else:
                # Update the maximum weight for the current segment
                mx = x
                
        return result