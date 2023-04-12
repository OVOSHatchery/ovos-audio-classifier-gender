import datetime
from precise_trainer import PreciseTrainer, ModelParams


extra_metrics = False
no_validation = False
freeze_till = 0
sensitivity = 0.2
if not 0.0 <= sensitivity <= 1.0:
    raise ValueError('sensitivity must be between 0.0 and 1.0')
params = ModelParams(skip_acc=no_validation, extra_metrics=extra_metrics,
                     loss_bias=1.0 - sensitivity, freeze_till=freeze_till)
model_name = "male_ww"
folder = "/tmp/male_ww"
model_path = f"/home/miro/PycharmProjects/ovos-audio-classifiers/trained/{model_name}"
log_dir = f"logs/fit/{model_name}/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

trainer = PreciseTrainer(model_path, folder, epochs=100, log_dir=log_dir)
# look for best hyperparams during a few cycles
# model_file = trainer.train_optimized(cycles=20)
# train the best model for more epochs
# trainer.train_epochs = 5000
model_file = trainer.train()
trainer.test(model_file, folder)
