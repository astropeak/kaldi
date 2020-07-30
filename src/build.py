import os
import shutil
import random
import vcjobs.core.vcjobfactory as vcjobfactory
import vcjobs.utils as vcutil

outdir = 'outdir'
if os.path.exists(outdir):
  shutil.rmtree(outdir, ignore_errors=False, onerror=None)

env = dict(vcutil.getDefaultEnv())
env = dict(os.environ)
sge = vcjobfactory.SGE(**dict(vcutil.getDefaultSge()))

# to run jobs on the grid, pass a sge parameter when createing factory
factory = vcjobfactory.VoConJobFactory(outdir+'/log/',env=env,maxjobs=100,sge=sge)


commands = ['make -j 8']
factory.createVCJob('cat_job', commands, [], [])


# launch all jobs
factory.launch()
