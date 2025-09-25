import ROOT as r
import sys

def python_example(samples=10000):
    # Histogram filled with a normal distribution
    #r.gStyle.SetOptStat(0)  # turn off default stats box in histograms
    
    tr = r.TRandom3()
    hist1 = r.TH1F("hist1","random gauss;x;frequency",100,50,150) # axis name, plot name, bins, xmin, xmax
    fpeak = r.TF1("fpeak","exp(-0.5*(x-[0])*(x-[0])/[1]/[1])",50,150)
    fpeak.SetParameters(100,6)
    hist1.FillRandom("fpeak",samples)
    tc1 = r.TCanvas("c1","Canvas1")
    hist1.Draw("e")
    tc1.Update()

    # A multi panel plot
    tc2 = r.TCanvas("c2","Canvas2")
    tc2.Divide(2,2)  # divide in to 2x2 panels
    tc2.cd(1)
    hist1.Draw("e")

    # add a random uniform offset to the histogram
    hist2 = hist1.Clone("hist2")
    hist2.SetTitle("Gauss+offset;x;frequency")
    for i in range(samples//3):
        hist2.Fill(tr.Uniform(50,150))
    tc2.cd(2)
    hist2.Draw("e")

    # apply an offset to give us a 1/x^2 baseline
    hist3 = hist1.Clone("hist3")
    hist3.SetTitle("Gauss+offset2;x;frequency")
    base2 = r.TF1("base2","1/x/x",1,10)
    for i in range(samples*30):
        x = base2.GetRandom()*10+40;
        hist3.Fill(x)
    tc2.cd(3).SetLogy()
    hist3.Draw("e")

    # a double gaussian
    hist4 = hist1.Clone("hist4")
    hist4.SetTitle("Double Gaussian;x;frequency")
    fpeak.SetParameter(1,20)
    hist4.FillRandom("fpeak",samples//2)
    tc2.cd(4)
    hist4.Draw("e")

    tc2.Update()
    input("hit 'return' to continue")

    # save our plot outputs
    # tc1.SaveAs("canvas1.png")
    tc2.SaveAs("canvas2d_py.png")
    
if __name__ == '__main__':
    samples=10000
    if len(sys.argv)>1: samples=int(sys.argv[1])
    python_example(samples)
