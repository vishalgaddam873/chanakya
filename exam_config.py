config = {
    "question_config" :{
                "category-1":{
                    "easy":1,
                    "medium":2,
                    "hard":2
                },
                "category-2":{
                    "easy":1,
                    "medium":1,
                    "hard":1
                },
                "category-3":{
                    "easy":0,
                    "medium":1,
                    "hard":2
                },
                "category-4":{
                    "easy":1,
                    "medium":1,
                    "hard":2
                }
    },
    "marks_config" :{
                        "easy":(1,0),
                        "medium":(2,0),
                        "hard":(3,0)
    },
    "test_config":{
                    "test_time":60*60 + 5 #1 hour + 5 (for N/W delay and all)
    }
}