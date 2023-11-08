class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy :
            if t==1 :
                return False
            return True
            
        elif sx==fx  :
            dist=abs(sy-fy) 
            if dist<=t :
                return True 
            return False 
        elif sy==fy :
            dist=abs(sx-fx)
            if dist<=t :
                return True 
            return False 
        else :
            x_dist=abs(sx-fx)
            y_dist=abs(sy-fy)
            if y_dist<=x_dist :
                if x_dist<=t :
                    return True 
                return False 
            else :
                if y_dist<=t :
                    return True 
                return False

        