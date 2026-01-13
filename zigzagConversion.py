# accepted variant
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1: return s

        M = 1000
        A = [ ['']*M for i in range(numRows) ]

        k=0
        for i in range(M): 
            if i%2 == 0:
                for j in range(numRows):
                    if k<len(s):
                        A[j][i]=s[k]
                        k=k+1
                    else: break
            else:
                for j in range(numRows-2, 0, -1):
                    if k<len(s):
                        A[j][i]=s[k]
                        k=k+1
                    else: break

        result = ''
        for j in range(numRows):
            for i in range(M):
                result = result + A[j][i] 
        return result
    
# # first variant
# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         if numRows==1: return s

#         M = 1000
#         A = [ ['a']*M for i in range(numRows) ]

#         k=0
#         for i in range(M): 
#             print('i=', i)
#             if i%(numRows-1) == 0:
#                 for j in range(numRows):
#                     if k<len(s):
#                         A[j][i]=s[k]
#                         k=k+1
#                     else: A[j][i]=''
#                     print('j=', j, ' ', A[j][i])
#             else:
#                 for j in range(numRows):
#                     if (i+j) % (numRows-1) != 0:
#                         A[j][i]=''
#                     else: 			
#                         if k<len(s):
#                             A[j][i]=s[k]
#                             k=k+1
#                         else: A[j][i]=''
#                     print('j=', j, ' ', A[j][i])

#         result = ''
#         for j in range(numRows):
#             for i in range(M):
#                 result = result + A[j][i] 
#         return result
