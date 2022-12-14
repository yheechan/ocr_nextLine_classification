import torch

def graphModel(dataloader, model, writer):
    # Again, grab a single mini-batch of images
    dataiter = iter(dataloader)
    first, second, labels = dataiter.next()

    # add_graph() will trace the sample input through your model,
    # and render it as a graph.
    writer.add_graph(model.cpu(), (first, second))
    writer.flush()

    print('uploaded model graph to tensorboard!')

def saveModel(fn, model):
    model.cpu()
    torch.save(model, '../models/'+fn+'.pt')

def getModel(fn):
    model = torch.load('../models/'+fn+'.pt')
    return model