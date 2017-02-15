class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        s_list = list(s)
        if not s_list:
            return ''
        else:
            result = []
            while s_list[0] == ' ':
                del s_list[0]
                if not s_list:
                    return ''
            while s_list[-1] == ' ':
                del s_list[-1]
                if not s_list:
                    return ''
            if not s_list:
                return ''
            else:
                i = 0
                s_len = len(s_list)
                while s_list[i]:
                    if s_list[i] == ' ':
                        if s_list[i-1] == ' ':
                            del s_list[i]
                            i -= 1
                    i += 1
                    s_len = len(s_list)
                    if i == s_len:
                        break

                tail = len(s_list)
                for i in range(len(s_list)):
                    if s_list[-i-1] == ' ':
                        if tail == len(s_list):
                            result.extend(s_list[len(s_list)-i:len(s_list)])
                            result.append(' ')
                            tail = len(s_list)-i-1
                        else:
                            result.extend(s_list[len(s_list)-i:tail])
                            result.append(' ')
                            tail = len(s_list)-i-1
                result.extend(s_list[0:tail])
            return "".join(result)