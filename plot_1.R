delaysecs <- function() {
    delaysecs=read.table('part1-delaysecs.txt',header=TRUE,sep="\t")
    sim_mins <- delaysecs[,1]/60
    plot(
        sim_mins,
        delaysecs[,2],
        type="l", lty=1,
        xlab="Simulation time (mins)",
        ylab="Ethernet Delay (secs)",
        main="Lab2: Small Internetworks\nEthernet Delay for the whole network",
        col="red"
    )

    lines(sim_mins, delaysecs[,3], col="blue", lty=1 )
    lines(sim_mins, delaysecs[,4], col="green",lty=1 )

    legend("bottomright", inset=.05, c("First Floor","Second Floor Expansion 1","Second Floor Expansion 2"), lty=1, col=c("red","blue","green"))
}

loadbps <- function() {
    loadbps=read.table('part1-loadbps.txt',header=TRUE,sep="\t")
    sim_mins <- loadbps[,1]/60
    plot(
        sim_mins,
        loadbps[,2],
        type="l", lty=1,
        xlab="Simulation time (mins)",
        ylab="Load (bits/sec)",
        main="Lab2: Small Internetworks\nServer Load",
        col="red",
        ylim=c(0,12500)
    )

    lines(sim_mins, loadbps[,3], col="blue", lty=1 )
    lines(sim_mins, loadbps[,4], col="green",lty=1 )

    legend("topright", inset=.05, c("First Floor","Second Floor Expansion 1","Second Floor Expansion 2"), lty=1, col=c("red","blue","green"))
}

#loadbps()
delaysecs()
