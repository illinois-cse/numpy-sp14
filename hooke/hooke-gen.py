import numpy

m = numpy.linspace(0,2000,51)
k = 0.008
F = m/1000 + numpy.random.normal(0,0.01,size=m.shape)
F[0] = 0
d = F/k
data = numpy.vstack((m,d)).T
numpy.savetxt('./spring.data',data,fmt='%12.6g')
