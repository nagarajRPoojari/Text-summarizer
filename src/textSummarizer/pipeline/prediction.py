from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        self.pipe = pipeline("summarization", model=self.config.model_path, tokenizer=self.tokenizer)
    
    def segment_text_into_groups(self, text, group_size):
        words = text.split()
        word_groups = [words[i:i+group_size] for i in range(0, len(words), group_size)]
        return [' '.join(group) for group in word_groups]
    
    def predict(self, text):
        gen_kwargs = {"length_penalty": 0.2, "num_beams": 2, "max_length": 128, "min_length": 50}


        group_size = 600  

        word_groups = self.segment_text_into_groups(text, group_size)
        
        summaries = []
        for group in word_groups:   
            res=self.pipe(group, **gen_kwargs) 
            print(res)        
            group_summary = res[0]["summary_text"]
            summaries.append(group_summary)


        combined_summary = "\n".join(summaries)
        
        
        if len(combined_summary.split())>500:
            combined_summary = self.predict(combined_summary)
        

        return combined_summary