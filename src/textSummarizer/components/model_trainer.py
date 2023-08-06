from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import ModelTrainerConfig
import os
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import tensorflow as tf

class ModelTrainer:
    def __init__(self,
                 config:ModelTrainerConfig):
        
        self.config=config
    
    def train(self):
        
        tokenizer=AutoTokenizer.from_pretrained(self.config.model_ckpt)
        pegasus_model=AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
        data_collector=DataCollatorForSeq2Seq(tokenizer=tokenizer, model=pegasus_model)
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        
        ##trainer_args = TrainingArguments(
        ##    output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
        ##    per_device_train_batch_size=1, per_device_eval_batch_size=1,
        ##    weight_decay=0.01, logging_steps=10,
        ##    evaluation_strategy='steps', eval_steps=500, save_steps=1e6,
        ##    gradient_accumulation_steps=16
        ##) 
 
        
        
        ##trainer = Trainer(model=pegasus_model, args=trainer_args,
        ##          tokenizer=tokenizer, data_collator=data_collector,
        ##          train_dataset=dataset_samsum_pt["train"], 
        ##          eval_dataset=dataset_samsum_pt["validation"])
        
        ##trainer.train()
        
        pegasus_model.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))