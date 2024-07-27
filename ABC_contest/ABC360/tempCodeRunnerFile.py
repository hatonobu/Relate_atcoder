    x,y = XY[i]
            x2,y2 = XY[j]

            if (x,y2) in check:
                if (x2,y) in check:
                    ans += 1