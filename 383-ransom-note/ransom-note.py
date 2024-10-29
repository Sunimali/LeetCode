class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        mag_dict = {}

        #iterate through the magazine
        for i in magazine:
            if i in mag_dict:
                mag_dict[i] = mag_dict[i]+ 1#increment the value
            else:
                mag_dict[i] = 1 #add new key to to the dictoinary

        #iterate through the ransom note
        for i in ransomNote:
            if i in mag_dict:
                if(mag_dict[i]>0):
                    mag_dict[i] = mag_dict[i] - 1 #decrease the count the character
                else:
                    return False #no remaining for that character    
            else:
                return False   #character not found 
        return True #if pass all then all chracters found