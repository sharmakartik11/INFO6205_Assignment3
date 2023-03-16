class Solution:
    def hasPath(self, maze: [int], start: [int], destination: [int]) -> bool:

        visited = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dest = (destination[0], destination[1])

        def startFrom(pos):
            newStops = []
            for d in directions:
                newX = pos[0]
                newY = pos[1]
                while (True):
                    possibleNewX = newX + d[0]
                    possibleNewY = newY + d[1]
                    if (possibleNewX >= 0 and possibleNewX < len(maze)) and (
                            possibleNewY >= 0 and possibleNewY < len(maze[0])) and (
                            maze[possibleNewX][possibleNewY] != 1):
                        newX = possibleNewX
                        newY = possibleNewY
                        continue
                    else:
                        break
                newStop = (newX, newY)
                if newStop == dest:
                    return True
                newStops.append(newStop)

            visited.append(pos)

            for newStop in newStops:
                if newStop not in visited:
                    if startFrom(newStop):
                        return True
            return False

        startPos = (start[0], start[1])
        return startFrom(startPos)

s = Solution()
print(s.hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4]))