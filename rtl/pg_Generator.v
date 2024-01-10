`timescale 1ns/1ps

module pg_Generator(
    input [127:0] x,
    input [127:0] y,
    output [127:0] p,
    output [127:0] g
);

    // pg_Gen pg0(x[0], y[0], p[0], g[0]);
    // generate instantiate pg_Gen for each bit of the vectors
    genvar i;
    generate
        for (i = 0; i < 128; i = i + 1) begin
            pg_Gen pg_inst (
                .x(x[i]),
                .y(y[i]),
                .p(p[i]),
                .g(g[i])
            );
        end
    endgenerate
endmodule

// ######## module for individual pg_Gen ######################
module pg_Gen(
    input x,
    input y,
    output p,
    output g
);

    // used in pg_Generator
    assign p = x ^ y;
    assign g = x & y;

endmodule