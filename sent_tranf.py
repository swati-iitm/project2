from sentence_transformers import  SentenceTransformer, util
import json 

model = SentenceTransformer('all-MiniLM-L6-v2')

class MatchQuestion:
    def __init__(self):
        with open("question_mapper.json",'r') as f:
            self.question_bank = list(json.load(f).keys())
        self.question_bank_embeddings=model.encode(self.question_bank, convert_to_tensor=True)

    def match_question(self,ques):
        ques_embedding = model.encode(ques, convert_to_tensor=True)
        similarities = util.pytorch_cos_sim(ques_embedding, self.question_bank_embeddings)
        most_similar_idx = similarities.argmax().item()
        print(most_similar_idx)
        return self.question_bank[most_similar_idx]